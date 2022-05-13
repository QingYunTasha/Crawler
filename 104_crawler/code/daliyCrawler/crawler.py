# -*- coding: utf-8 -*-
import requests
import time

def crawler104():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36", 
               "Referer": "https://www.104.com.tw/jobs/search/"}
    
    url = "https://www.104.com.tw/jobs/search/list?"
    
    areas = ('6001001001','6001001002','6001001003','6001001004','6001001005','6001001006','6001001007',
             '6001001008','6001001009','6001001010','6001001011','6001001012',
             '6001002001','6001002003','6001002005','6001002007','6001002009','6001002011','6001002013',
             '6001002015','6001002017','6001002019','6001002021','6001002023','6001002025','6001002027',
             '6001002029','6001002002','6001002004','6001002006','6001002008','6001002010','6001002012',
             '6001002014','6001002016','6001002018','6001002020','6001002022','6001002024','6001002026',
             '6001002028','6001005000','6001008000','6001014000','6001016000','6001006001','6001006002',
             '6001006003','6001006004','6001006005','6001006006','6001006007','6001006008','6001006009',
             '6001006010','6001006011','6001006012','6001006013','6001006014','6001007000','6001003000',
             '6001010000','6001013000','6001012000','6001011000','6001019000','6001020000','6001018000')
    
    params = "ro=1&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm\
            &mode=s&jobsource=2018indexpoc&order=1&asc=0&jobcat=2007000000"
    
    applyAnalyze_url = "https://www.104.com.tw/jb/104i/applyAnalysisToJob/all?job_no="
    
    job_url = "https://www.104.com.tw/job/ajax/content/"
    
    All_Data = []
    
    for area in areas:
        params_area = f"{params}&area={area}"
        
        #find total page
        r = requests.get(url + params_area, headers=headers)
        while r.status_code != 200:
            r = requests.get(url + params_area, headers=headers)
        data = r.json()
        total_page = data['data']['totalPage']
        
        for page in range(1, total_page + 1):
            paramsNow = f"{params_area}&page={page}"
            r = requests.get(url + paramsNow, headers=headers)
            while r.status_code != 200:
                r = requests.get(url + paramsNow, headers=headers)
            data = r.json()
            for job in data['data']['list']:
                attemp = 0
                while attemp < 3:
                    try:
                        job_id = job['link']['job'][21: 26]
                        job_r = requests.get(job_url + job_id, headers=headers)
                        while job_r.status_code != 200:
                            job_r = requests.get(job_url + job_id, headers=headers)
                        job_content = job_r.json()['data']
                        time.sleep(.15)
                    
                        job_applyAnalyze_id = job['jobNo']
                        job_apply_r = requests.get(applyAnalyze_url + job_applyAnalyze_id, headers=headers)
                        while job_apply_r.status_code != 200:
                            job_apply_r = requests.get(applyAnalyze_url + job_applyAnalyze_id, headers=headers)    
                        job_apply_content = job_apply_r.json()
                        time.sleep(.08)
                        
                        All_Data.append((job_content, job_apply_content))
                        attemp = 3
    
                    except KeyboardInterrupt:
                        break
                    except:
                        attemp += 1
            print(f"page{page} is done!!")

    import json
    today = time.strftime("%Y_%m_%d") + ".json"
    
    with open(today, 'w', encoding = 'UTF-8') as outfile:  
        json.dump(All_Data, outfile, ensure_ascii=False, indent=2)


# =============================================================================
# #準備訊息物件設定
# #載入模組            
# import email.message
# #建立訊息物件
# msg=email.message.EmailMessage()
# #利用物件建立基本設定
# 
# 
# 
# msg["From"]="tashaqymail@gmail.com"
# msg["To"]="rivendinner@gmail.com"
# 
# msg["Subject"]= f"success{today}"
# 
# #寄送郵件主要內容
# #msg.set_content("測試郵件純文字內容") #純文字信件內容
# msg.add_alternative("<h3>HTML內容</h3>",subtype="html") #HTML信件內容
# 
# acc="tashaqymail@gmail.com"
# password='dieeid8181'
# 
# #連線到SMTP Sevver
# import smtplib
# #可以從網路上找到主機名稱和連線埠
# server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連驗
# server.login(acc,password)
# server.send_message(msg)
# server.close() #發送完成後關閉連線        
# =============================================================================
            
                

