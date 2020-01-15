import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.weather.go.kr/weather/forecast/mid-term_01.jsp")
# https://www.weather.go.kr/w/wnuri-fct/weather/today-vshortmid.do?code=4825058000&unit=km%2Fh
# response = requests.get("https://www.weather.go.kr/w/weather/today.do")

html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')

table_midterm = soup.find_all("table",{"class":"table_midterm"})
table1 = table_midterm[1]
# print(table1)
table1_thead = table1.find("thead")
table1_thead_day = table1_thead.find_all("th")
# print(table1_thead)
for tmp in table1_thead:
    table1_thead_day = tmp.find_all("th")
    for tmp2 in table1_thead_day:
        print(tmp2.text)



print("Rmx")