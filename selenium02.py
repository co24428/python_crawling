from selenium import webdriver
from bs4 import BeautifulSoup
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

driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
# driver.find_element_by_name("email").send_keys('20191216')
driver.execute_script("document.getElementsByName('pw')[0].value='20191216'")
# driver.find_element_by_name("pw").send_keys('20191216')
login_btn = driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input')
login_btn.click()

time.sleep(3)
driver.execute_script("alert('hello')")

"""
driver.get("http://daum.net") # 로그인 이후의 페이지
html = driver.page_source
soup = BeautifulSoup(html, 'html_parser')
driver.close()
"""