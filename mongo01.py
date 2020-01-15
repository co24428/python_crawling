import pymongo
import json
import requests

# 1. 접속
conn = pymongo.MongoClient('192.168.99.100', 32766)
# 2. db 연결
db = conn.get_database("db1") # Database 있으면 가져오고, 없으면 만들고
# 3. 테이블 연결
table = db.get_collection("table1") # Collection 있으면 가져오고, 없으면 만들고

dict1 = {"id": "a12","name":"n12", "age": 133}
# 4. 테이블에 데이터 삽입
table.insert_one(dict1) # 추가 - 추가해야 db가 만들어진다. # 추가 부분 주석처리


data1 = table.find()
print(type(data1)) # <class 'pymongo.cursor.Cursor'> -> for문을 써야 한다.
for tmp in data1:
    print(tmp)
