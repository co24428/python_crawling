# 인터넷(링크)을 통해 가져오기
import json
import requests
import cx_Oracle as oci
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

url = "http://ihongss.com/json/exam4.json"
str1 = requests.get(url).text 
data1 = json.loads(str1)

tmp_json = """
    {
        'name' : %s,
        'species' : %s,
        'like_food' : %s,
        'dislike_food' : %s
    } """
pet_dict = dict()


for i in data1:
    # print(i)
    print("="*50)
    name = i['name']
    species = i['species']
    like_food = i['foods']['likes'][0]
    dislike_food = i['foods']['dislikes'][0]
    print(tmp_json %(name, species, like_food, dislike_food))

