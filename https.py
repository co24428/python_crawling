import requests
import json

url = "https://www.datastore.or.kr/api/DataImage/getImageProductListExport"
str1 = requests.get(url, verify=False).text
data1 = json.loads(str1)[:10]

print(data1)