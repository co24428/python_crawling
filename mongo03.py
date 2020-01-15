import pymongo
import json
import requests

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1") 
col1 = db.get_collection("table1") 

# SELECT * FROM table1
data1 = col1.find()
for tmp in data1:
    print(tmp)
print("="*50)

# SELECT * FROM table1 WHERE ID='a'
data2 = col1.find({"id":"a"})
for tmp in data2:
    print(tmp)
print("="*50)

# SELECT ID,NAME FROM table1 WHERE ID='a'
data3 = col1.find({"id":"a"}, {"id":1, "name":1})
for tmp in data3:
    print(tmp)
print("="*50)

# SELECT * FROM table1 WHERE age > 10
data4 = col1.find({"age":{"$gt":10}})
for tmp in data4:
    print(tmp)
print("="*50)

# SELECT * FROM table1 ORDER BY name ASC
data5 = col1.find().sort('name',1)
for tmp in data5:
    print(tmp)
print("="*50)

# SELECT * FROM table1 WHERE age>=10 AND age<=30
data5 = col1.find({"age":{"$gte":10, "$lte":30}})
for tmp in data5:
    print(tmp)
print("="*50)

# SELECT COUNT(*) FROM table1
data7 = col1.find().count()
print(data7)
print("="*50)

# SELECT * FROM table1 WHERE ID='a' OR ID='b'
data = col1.find({"$or":[{"id":'a'},{"id":"a12"}]})
for tmp in data5:
    print(tmp)
print("="*50)

conn.close()

print("RMx")