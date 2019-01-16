from selenium import webdriver
import time
import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

print('go',os.path.abspath('.'))

# 加启动配置
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument('-headless')  # 无头参数
# 打开chrome浏览器

driver = webdriver.Chrome(chrome_options=option,executable_path='./selenium_crawl/chromedriver')
# driver = webdriver.PhantomJS(executable_path='./selenium_crawl/phantomjs')
driver.set_window_size(1366, 768)

driver.get('https://www.yuntongxun.com/user/login')
# print('source',driver.page_source)




# driver.maximize_window()
time.sleep(20)
driver.find_element_by_id('UN').send_keys(' ')
time.sleep(20)




#给用户名的输入框标红
js="var q=document.getElementById(\"loginPwd\");q.style.display=\"!none\";"
#调用js
driver.execute_script(js)

#定位到要悬停的元素
yes = driver.find_element_by_xpath('//*[@id="PWD"]')
print('yes',yes)

yes2 = driver.find_element_by_xpath('//*[@id="loginPwd"]')
print('yes2',yes2)


#对定位到的元素执行悬停操作
# ActionChains(driver).move_to_element(yes).perform()

driver.find_element_by_xpath('//*[@id="PWD"]').clear()
driver.find_element_by_xpath('//*[@id="PWD"]').send_keys(' ')

# driver.find_element_by_id("loginPwd").clear()
# driver.save_screenshot("loginPwd.png")
# driver.find_element_by_id("loginPwd").send_keys('a123456')
# ActionChains(driver).click(driver.find_element_by_id("PWD")).perform() #使用perform()才能执行action

# searchButtonElement = driver.find_element_by_id('loginBtn')
searchButtonElement =driver.find_element_by_xpath('//*[@id="loginBtn"]')

ActionChainsDriver = ActionChains(driver).click(searchButtonElement)
ActionChainsDriver.perform()   #执行perform()才会进行搜索
print('source',driver.page_source)
time.sleep(5)
driver.quit()





