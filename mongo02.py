import pymongo
import json
import requests

# 1. 접속
conn = pymongo.MongoClient('192.168.99.100', 32766)
# 2. db 연결
db = conn.get_database("db1") # Database 있으면 가져오고, 없으면 만들고
# 3. 테이블 연결
table = db.get_collection("table1") # Collection 있으면 가져오고, 없으면 만들고

url = "http://ihongss.com/json/exam4.json"
str1 = requests.get(url).text
data2 = json.loads(str1)

for tmp in data2:
    name = tmp['name']
    species = tmp['species']
    foods = tmp['foods']

    dict1 = dict()
    dict1['name'] = tmp['name']
    dict1['species'] = tmp['species']
    dict1['likes'] = tmp['foods']['likes'][0]
    dict1['dislikes'] = tmp['foods']['dislikes'][0]
    # table.insert_one(dict1) # 추가 부분 주석처리


conn.close()

print("RMx")