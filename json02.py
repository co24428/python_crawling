# 인터넷(링크)을 통해 가져오기
import json
import requests
import cx_Oracle as oci
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

url = "http://ihongss.com/json/exam2.json"
str1 = requests.get(url).text 

# print(str1)
# print(type(str1))  # str -> not json
# print("="*50)

data1 = json.loads(str1)
# print(data1)
# print(type(data1)) # dict
# print("="*50)

ret = data1["ret"]
ret1 = data1["ret1"]
# print(ret)
# print(type(ret))   # dict
ar = [ret, ret1]
for one in ar:
    sql = """
        INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
        VALUES(:ID, 'PASSWORD', :NAME, :AGE, SYSDATE)
        """
    # SQL에서는 열 값에 string을 표시할 때, '' single quote를 써야 한다.
    cursor.execute(sql, one)

conn.commit()
