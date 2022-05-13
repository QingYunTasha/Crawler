# -*- coding: utf-8 -*-
import pymysql

def insertJob(data: dict):
    db_settings = {
        "host": "localhost",
        "user": "root",
        "password": "dieeid8181",
        "db": "104_db",
        "charset": "utf8"
    }
    
    #connect mysql
    try:
        conn = pymysql.connect(**db_settings)
    except Exception as ex:
        print(ex)
    cursor = conn.cursor()
    
    for key, table in data.items():
        for job in table:
            command = "INSERT INTO " + key + " VALUES ("
            for col in job:
                if isinstance(col, str):
                    col = col.replace("'", '"')
                    command += "'" + col + "'" + ","
                else:
                    command += col + ","
            command = command[: -1]
            command += ");"
            
            cursor.execute(command)
            conn.commit()

