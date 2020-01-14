from bs4 import BeautifulSoup
import json
import requests

"""
<div class="tit3">
    <a href="/movie/bi/mi/basic.nhn?code=143435" title="옥자">옥자</a>
</div>
"""

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str = requests.get(url)
print(str.text)

soup = BeautifulSoup(str.text, 'html.parser')

one = soup.find_all("div", {"class": "tit3"})
print("="*50)

for tmp in one:
    print("="*50)
    print(tmp.find("a"))
    print(tmp.find("a").text)
    print(tmp.find("a").attrs) # dictionary