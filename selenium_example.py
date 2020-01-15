from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920x1080")
 
driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\chromedriver.exe", chrome_options=options)

# driver.get("http://python.org")
driver.get("http://daum.net")
# driver.get("https://www.weather.go.kr/w/index.do")

# time.sleep(5) # 5초 대기

driver.find_element_by_css_selector("#inner_login > a.link_login.link_kakaoid").click()

time.sleep(4)

driver.find_element_by_name("email").send_keys('ID')
driver.find_element_by_name("password").send_keys('password')

time.sleep(4) # 5초 대기

driver.find_element_by_css_selector("#login-form > fieldset > div.wrap_btn > button").click()


# menus = driver.find_elements_by_css_selector('#top > nav > ul')
# #top > nav > ul > li.docs-meta > a
# menu = None # Python(Default), PSF, Docs, PyPI, Jobs, Community
# for m in menus:
#     if m.text == "Jobs":
#         pypi = m
#     print(m.text)
 
# pypi.click()  # 클릭
 
# time.sleep(5) # 5초 대기
# driver.quit() # 브라우저 종료
#top > nav > ul
