import pandas as pd
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")
table = db.get_collection("csv_exam")

df = pd.read_csv('C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\resources\\exam1.csv', delimiter=",")

df = df.dropna() 
print(df)
# print(df.keys())
keys = df.keys()

list1 = df.values.tolist() 

for person in list1:
    new_dict = dict()
    index = 0
    for j in keys:
        new_dict[j] = person[index]
        index += 1
    # print(new_dict)
    table.insert_one(new_dict)
    
print("="*50)

data1 = table.find()
for tmp in data1:
    print(tmp)
