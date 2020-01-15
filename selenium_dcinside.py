from selenium import webdriver
import time

options = webdriver.ChromeOptions()

options.add_argument('headless') 
options.add_argument("window-size=1920x1080")

driver = webdriver.Chrome("C:\\Users\\admin\\Desktop\\python_crawling\\python_crawling\\chromedriver.exe", options=options)

# driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver") 
# time.sleep(3)

# tag = driver.find_element_by_class_name('rank_top1000_list').find_elements_by_tag_name("a")

# print(tag)


driver.get("https://www.dcinside.com/")
time.sleep(3)

# 안됨, 
# 시도 순서는 selector > xpath > full xpath, 보통 xpath 선에서 마무리 된다. 
# 다 해도 안되면 안된다 생각하자

print("major ranking")
major_gall = driver.find_element_by_xpath('//*[@id="rank_gall"]/ol[6]')
major_gall_li = major_gall.find_elements_by_tag_name('li')
for tmp in major_gall_li:
    ranking = tmp.find_element_by_class_name("rank_txt")
    print("="*50)
    print(ranking.text)
    
minor_gall = driver.find_element_by_xpath('//*[@id="rank_gall"]/div[1]/span/a[2]')
minor_gall.click()
time.sleep(5)

print("minor ranking")
minor_gall = driver.find_element_by_xpath('//*[@id="rank_gall"]/ol[1]')
minor_gall_li = minor_gall.find_elements_by_tag_name('li')
for tmp in minor_gall_li:
    ranking = tmp.find_element_by_class_name("rank_txt")
    print("="*50)
    print(ranking.text)

# full xpath
#'/html/body/div[2]/main/div/section[2]/article[1]/div/ol[1]'



