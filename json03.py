# 인터넷(링크)을 통해 가져오기
import json
import requests
import cx_Oracle as oci
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

url = "http://ihongss.com/json/exam3.json"
str1 = requests.get(url).text 
data1 = json.loads(str1)


for i in data1:
    # print(data1[i]) # dictionary를 for 돌리면 key값이 나온다.
    for one in data1[i]:
        sql = """
        INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
        VALUES(:ID, 'PASSWORD', :NAME, :AGE, SYSDATE)
        """
        cursor.execute(sql, one)
        print(one)


conn.commit()