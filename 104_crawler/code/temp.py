#data list predeal
listdata = ['welfareTag', 'major']

lstdictdata = {'certificate': 'name', 'skill': 'description', 'specialty': 'description',
               'jobCategory': 'description'}        

lstlstdictdata = {'language': ['language', 'ability']}

applydata = {'Acert': 'certName', 'Aedu': 'eduName', 'Aexp': 'expName', 'Amajor': 'majorName',
             'Asex': 'sexName', 'Askill': 'skillName', 'AyearRange': 'yearRangeName'}

applyLdata = {'Alanguage': ['langName', ['levelName', 'count']]}

#create sql table script
scriptDict = {}
First = "CREATE TABLE "
Second = "("
cF = "`"
cS = " "
cT = ","
End = ");"

varType = "bit"
for name in listdata:
    tempSet = set()
    nameList = data[name]
    for row in nameList:
        for val in row:
            tempSet.add(val)
    script = First + name + Second
    for n in tempSet:
        n = n.replace(' ', '')
        script = script + cF + n + cF + cS + varType + cT
    script = script[: -1] + End
    scriptDict[name] = script

varType = "bit"
for name in lstdictdata:
    tempSet = set()
    nameList = data[name]
    for row in nameList:
        for dct in row:
            tempSet.add(dct[lstdictdata[name]])
    script = First + name + Second
    for n in tempSet:
        n = n.replace(' ', '')
        script = script + cF + n + cF + cS + varType + cT
    script = script[: -1] + End
    scriptDict[name] = script
    
varType = "TINYINT"
for name in lstlstdictdata:
    tempSet = set()
    nameList = data[name]
    for row in nameList:
        for dct in row:
            language = dct['language']
            for sep in ['listen', 'speak', 'read', 'write']:
                tempSet.add(language + sep)
    script = First + name + Second
    for n in tempSet:
        n = n.replace(' ', '')
        script = script + cF + n + cF + cS + varType + cT
    script = script[: -1] + End
    scriptDict[name] = script    
    
#apply
varType = "SMALLINT"

tempSet = set()
tempSet.add('total')
nameList = data['Alanguage']
for row in nameList:
    for key in row.keys():
        if key == 'total' or key == 'update_time':
            continue
        dct = row[key]
        val = dct['langName']
        for val2 in ['low', 'medium', 'high']:
            tempSet.add(val + val2)
script = First + 'Alanguage' + Second
for n in tempSet:
    n = n.replace(' ', '')
    script = script + cF + n + cF + cS + varType + cT
script = script[: -1] + End
scriptDict['Alanguage'] = script

#apply
varType = "SMALLINT"
for name in applydata:
    tempSet = set()
    tempSet.add('total')
    nameList = data[name]
    for row in nameList:
        for key in row.keys():
            if key == 'total' or key == 'update_time':
                continue
            dct = row[key]
            tempSet.add(dct[applydata[name]])
    script = First + name + Second
    for n in tempSet:
        n = n.replace(' ', '')
        script = script + cF + n + cF + cS + varType + cT
    script = script[: -1] + End
    scriptDict[name] = script
  
#connect mysql
import pymysql

db_settings = {
    "host": "localhost",
    "user": "root",
    "password": "dieeid8181",
    "db": "104_db",
    "charset": "utf8"
}

try:
    conn = pymysql.connect(**db_settings)
except Exception as ex:
    print(ex)
cursor = conn.cursor()

for sql in scriptDict.values():
    try:
        cursor.execute(sql)
    except:
        continue