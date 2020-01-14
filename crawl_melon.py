import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.melon.com/new/index.htm")

html = response.text
print(html)
soup = BeautifulSoup(html, 'html.parser')

div_them = soup.find_all("div",{"class":"ellipsis rank01"})



print("Rmx")