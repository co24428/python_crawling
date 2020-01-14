from bs4 import BeautifulSoup

# with open('./resources/exam1.html') as fp:
with open('C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\resources\\exam1.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # 1개 찾기
    one_divs = soup.find("div")
    print(one_divs)
    print("="*50)

    # 특정 클래스 찾기
    first_divs = soup.find_all("div",{"class":"first"})
    print(first_divs)
    print("="*50)

    # 내부로 들어가기 
    all_divs = soup.find_all("div")
    print(all_divs) # list [<></>,  <></>,  <></> ...]
    print("="*50)
    for tmp in all_divs: # <> ... </>
        print(type(tmp)) # <class 'bs4.element.Tag'>
        print(tmp)
        print("="*50)
        all_p = tmp.find_all("p")
        print(all_p)
        print("="*50)
        for tmp1 in all_p:
            print(tmp1)
            print(tmp1.text)