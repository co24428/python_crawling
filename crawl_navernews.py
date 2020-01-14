import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=731")

html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')

div_all = soup.find("ul",{"class":"type06_headline"})
# print(div_all)
dl_all = div_all.find_all("dl")
# print(dl_all)
for tmp in dl_all:
    dt_want = tmp.find_all("dt")[1]
    print(dt_want.text.strip())



print("Rmx")