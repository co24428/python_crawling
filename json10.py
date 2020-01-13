import pymongo
import json
import requests

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db10")
table = db.get_collection("exam10")

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1)

# ret = "y"

# if data1["ret"] =="y":
print(data1)
print("="*50)
print(data1["data"])
for one in data1["data"]: # {'id': 'id1', 'name': '가나다1', 'age': 31, 'score': {'math': 50, 'eng': 90, 'kor': 69}}
    dict1 = dict()

    dict1["id"] = one["id"]
    dict1["name"] = one["name"]
    dict1["age"] = one["age"]
    dict1["math"] = one["score"]["math"]
    dict1["kor"] = one["score"]["kor"]
    table.insert_one(dict1)
# else:
#     print("wrong ret")
