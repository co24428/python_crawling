from selenium import webdriver
import urllib. request

options = webdriver.ChromeOptions()

# options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')


driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\chromedriver.exe", chrome_options=options)

url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=091&aid=0007750912"
driver.get(url)

# selector > #image_view_0
img = driver.find_element_by_css_selector("#articleBodyContents > span.end_photo_org > img")
# print(img)


file = img.get_attribute("src") # 찾은 태그 중에서 src의 값 
print(file)
urllib.request.urlretrieve(file, "./python_crawling/img/a2.png")








