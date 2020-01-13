# 파일을 통해 가져오기
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")

cursor = conn.cursor()

# file1 = open('./resources/exam1.json')
file1 = open('./resources/exam2.json')

data1 = json.load(file1)
# print(data1)
# print(type(data1)) # dictionary

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    """
cursor.execute(sql, data1)
conn.commit()
