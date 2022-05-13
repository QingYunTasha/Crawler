# -*- coding: utf-8 -*-
import json

def convertSql(data: dict, majorJsPth: str) -> dict:
    tables = ['main', 'applicant', 'corp', 'major']
    res = {table: [] for table in tables}
    
    mainC = ['jobName', 'id', 'date', 'addressRegion', 'jobDescription', 'workExp']
    
    #Undefined name
    #major
    with open(majorJsPth, 'r') as f:
        majorDict = json.load(f)
        
    majorNew = {}
    for job in data.values():
        majorlist = job['major']
        for major in majorlist:
            if major not in majorDict:
                majorDict['index'] += 1
                index = majorDict['index']
                majorDict[major] = index
                majorNew[index] = (index, major)
            
    with open(majorJsPth, 'w') as f:
        json.dump(majorDict, f)
    
    #main
    corpNew = {}        
    for job in data.values():
        
        #major
        major = majorCnv(job['major'], majorDict)
        #lang
        language = langCnv(job['language'])
        #coporation
        corp = corpCnv(job, corpNew)
        #applicant
        applicant = appliCnv(job)
        #main
        main = [job[val] for val in mainC] + [major, language, corp]
        
        res['main'].append(main)
        res['applicant'].append(applicant)
    res['corp'] = list(corpNew.values())
    res['major'] = list(majorNew.values())
    
    return res

def majorCnv(majorR: list, majorDict: dict) -> str:
    if majorR is None: return ''
    
    major = ''
    for mj in majorR:
        major = major + str(majorDict[mj]) + ','

    #remove the last ,
    major = major[: -1]
    
    return major

def langCnv(langR: list) -> str:
    if langR is None: return ''
    
    lang = ''
    for lg in langR:
        lang = lang + lg['language'] + ': ' + lg['ability'] + ' '

    return lang

def corpCnv(job: dict, corpNew: dict) -> str:
    if job['custName'] is None: return ''
    
    key = job['custName'] + job['date']
    if key not in corpNew:
        corpNew[key] = tuple([job['date'], job['custName'], job['employees']])
                             
    return job['custName']

def appliCnv(job: dict) -> tuple:
    total = int(job['Aedu']['total'])
    #edu
    edu = ''
    eduDict = job['Aedu']
    for e in range(7):
        e = eduDict[str(e)]
        edu += e['eduName'] + ': ' + str(e['count']) + ','
    edu = edu[: -1]
    #exp
    exp = ''
    expDict = job['Aexp']
    for e in range(9):
        e = expDict[str(e)]
        exp += e['expName'] + ': ' + str(e['count']) + ','
    exp = exp[: -1]
    
    return (job['id'], job['date'], edu, exp, total)
    
    