import time
import re
from datetime import datetime
from selenium import webdriver
from xiaoxi import sendGL
def caozuo(name,password):
    url='https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin'
    #browser=webdriver.Chrome()
    browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    browser.implicitly_wait(10)
    browser.get(url)
    try:
        browser.find_element_by_id('username').click()
        browser.find_element_by_id('username').clear()
        browser.find_element_by_id('username').send_keys(name)
        browser.find_element_by_id('password').clear()
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_id('login').click()
        time.sleep(5)
        browser.find_element_by_id('report-submit-btn-a24').click()
        time.sleep(5)
        elements = browser.find_elements_by_xpath("//div//strong")
        lst=re.findall(r'-.*? ',elements[1].text)
        sbday=str(lst[0][4:6])
        sbday=int(sbday)
        #print(sbday)
        if sbday==datetime.now().day:
            print('上报成功')
            sendGL('上报成功',2084222530)
    except:
        print('未知错误')
        sendGL('未知错误',2084222530)
    browser.close()
#sendGL('123',2084222530)