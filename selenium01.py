from selenium import webdriver
import time

options = webdriver.ChromeOptions()


# options.add_argument('headless') # 화면표시 안된다.
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 
# driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\chromedriver.exe", chrome_options=options)

driver.get("http://ihongss.com/webboard")

driver.find_element_by_name("email").send_keys('20191216')
driver.find_element_by_name("pw").send_keys('20191216')

# find_element_by_css_selector => 1개 가져옴
login_btn = driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input')
login_btn.click()

# find_elements_by_css_selector => 여러 개 가져옴, 리스트 형식 
# some = driver.find_elements_by_css_selector('#form1 > div:nth-child(4) > input')
# some[0].click()


# 검사 후 해당 파트에서 > 우클릭 > copy > copy selector > #붙은거 그대로 사용
#form1 > div:nth-child(4) > input

