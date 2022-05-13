# -*- coding: utf-8 -*-
import crawler, retrieve, secRetrieve, insertJob
import os, shutil

data_path = r"C:\Users\QingYun\Desktop\rivendinner\Github\Crawler\104_crawler\data"

def main(data_path: str):
    os.chdir(data_path)
    crawler.crawler104()
    data = retrieve.retrieve(data_path)
    
    for stored_data in os.listdir():
        shutil.move(os.path.join(data_path, stored_data), os.path.join("../stored_data", stored_data))
    
    mjPath = r"C:\Users\QingYun\Desktop\rivendinner\Github\Crawler\104_crawler\code\daliyCrawler\majorDict.json"
    data = secRetrieve.convertSql(data, mjPath)   
    
    insertJob.insertJob(data)
    
    



if __name__ == "__main__":
    main(data_path)