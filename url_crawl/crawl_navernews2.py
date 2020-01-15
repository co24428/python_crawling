import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=731")

html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')

div_one = soup.find("div",{"class":"classfy sd"})
# print(div_one)

ul_all = div_one.find_all("ul",{"class":"list_txt"})
for tmp in ul_all:
    print("="*50)
    print(tmp)
    ul_all = div_one.find_all("ul",{"class":"list_txt"})

print("Rmx")