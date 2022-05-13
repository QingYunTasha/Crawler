# -*- coding: utf-8 -*-
import json, os

def retrieve(path: str) -> dict: 
    name = {'jobName': [0, 'header', 'jobName'],
            'appearDate': [0, 'header', 'appearDate'],
            'custName': [0, 'header', 'custName'],
            'industry': [0, 'industry'],
            'certificate': [0, 'condition', 'certificate'],
            'edu': [0, 'condition', 'edu'],
            'language': [0, 'condition', 'language'],###英文聽說讀寫
            'otherCondition': [0, 'condition', 'other'],
            'skill': [0, 'condition', 'skill'],
            'workExp': [0, 'condition', 'workExp'],
            'major': [0, 'condition', 'major'],
            'specialty': [0, 'condition', 'specialty'],##
            'employees': [0, 'employees'],
            'addressRegion': [0, 'jobDetail', 'addressRegion'],
            'businessTrip': [0, 'jobDetail', 'businessTrip'],
            'jobCategory': [0, 'jobDetail', 'jobCategory'],##
            'jobDescription': [0, 'jobDetail', 'jobDescription'],
            'remoteWork': [0, 'jobDetail', 'remoteWork'],
            'salaryMax': [0, 'jobDetail', 'salaryMax'],
            'salaryMin': [0, 'jobDetail', 'salaryMin'],
            'salaryType': [0, 'jobDetail', 'salaryType'],
            'welfareTag': [0, 'welfare', 'tag'],##
            'welfare': [0, 'welfare', 'welfare']}
    applyAnalyze = {'Acert': [1, 'cert'], ##
                    'Aedu': [1, 'edu'], ##
                    'Aexp': [1, 'exp'], ##
                    'Alanguage': [1, 'language'], ##
                    'Amajor': [1, 'major'], ##
                    'Asex': [1, 'sex'], ##
                    'Askill': [1, 'skill'], ##
                    'AyearRange': [1, 'yearRange']}
    
    #data predeal
    
    retrieved_data = {}
    os.chdir(path)
    for fname in os.listdir():
        f_date = fname[: 10]
        with open(os.path.join(path, fname), encoding='UTF-8') as f:
            data = json.load(f)   
        for job in data:
            try:
                id_ = job[0]['header']['analysisUrl'][-5: ]
                pKey = id_ + f_date
                dct = {}
                
                for column in name.keys():
                    value = job[0]
                    for i in name[column][1: ]:
                        value = value[i]
                    dct[column] = value
                for column in applyAnalyze.keys():
                    value = job[1]
                    for i in applyAnalyze[column][1: ]:
                        value = value[i]
                    dct[column] = value   
                
                dct['date'] = f_date
                dct['id'] = id_
                dct['pKey'] = pKey
                
                retrieved_data[pKey] = dct
            except:
                continue
            
    return retrieved_data

