import pymongo
import json
import requests
import cx_Oracle as oci

conn_o = oci.connect("admin/1234@192.168.99.100:32764/xe", encoding="utf-8")
cursor = conn_o.cursor()

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") 
col1 = db.get_collection("table1") 

# SELECT * FROM table1
data1 = col1.find()

for tmp in data1:
    print(tmp) 
    test = {"id":tmp['id'], "name":tmp['name'],"age":tmp['age']}
    sql = """
        INSERT INTO TABLE1(NO, ID, NAME, AGE)
        VALUES(SEQ_TABLE1_NO.nextval, :id, :name, :age)
    """
    cursor.execute(sql, test)
    conn_o.commit()


conn_o.close()
conn.close()

print("RMx")

"""
-- 시퀀스 생성
CREATE SEQUENCE SEQ_TABLE1_NO
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCACHE;
"""