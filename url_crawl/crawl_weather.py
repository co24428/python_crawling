import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.weather.go.kr/w/wnuri-fct/weather/today-vshortmid.do?code=1159068000&unit=km%2Fh")
# https://www.weather.go.kr/w/wnuri-fct/weather/today-vshortmid.do?code=4825058000&unit=km%2Fh
# response = requests.get("https://www.weather.go.kr/w/weather/today.do")

html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')

div_them = soup.find_all("div",{"class":"them"})
for tmp in div_them:
    # print(tmp)
    print("="*50)
    span_txt = tmp.find_all("span",{"class":"txt"})
    for tmp1 in span_txt:
        print(tmp1.text)


# for tag in soup.select('div[class=them]'):
#     print(tag.text)

# for tag in soup.select('span[class=tooltip]'):
#     print(tag.text)

# for tag in soup.select('div[class=tom-mark]'):
#     print(tag.text)

# for tag in soup.select('span[class=tmn]'):
#     print(tag.text)

# for tag in soup.select('span[class=tmx]'):
#     print(tag.text)

print("Rmx")