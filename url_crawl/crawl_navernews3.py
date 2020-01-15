from bs4 import BeautifulSoup
import requests


url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=227"
str = requests.get(url)
# print(str.text)


soup = BeautifulSoup(str.text, 'html.parser')

all_div_section = soup.find_all('ul', {"class":"section_list_ranking"})
# print(all_div_section)
for tmp in all_div_section:
    li_all = tmp.find_all("li")
    # print("="*50)
    # print(li_all[0]) # 전체 섹션의 1위 기사 0~9 : 1위~10위
    #정치: 0, 경제: 1, 사회: 2, 생활/경제: 3, 세계: 4, IT/과학: 5 => rank가 앞에, section이 뒤에
    section = 0
    for i in range(0,10):
        print(li_all[i].text)
    print("="*50)