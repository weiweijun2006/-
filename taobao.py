import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from config import *
import pymongo
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_TABLE = 'product'

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

NAME = 'xxx'
PSWD = 'xxx'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

browser = webdriver.Chrome(service_args=SERVICE_ARGS)#PhantomJS
wait = WebDriverWait(browser, 10)

browser.set_window_size(1400, 900)




def logintaobao():
        print('准备登陆')
    #try:
        browser.get('https://login.taobao.com/member/login.jhtml')
        content =browser.find_elements_by_xpath('//*[@id="J_LoginBox"]')

        if(content[0].get_attribute("class")=="login-box no-longlogin module-quick"):
            submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_Quick2Static')))
            submit.click()


        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_username_1')))
        input2 = wait.until( EC.presence_of_element_located((By.CSS_SELECTOR, '#TPL_password_1')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SubmitStatic')))
        submit.click()#J_SelectAll1
        input.send_keys(NAME)#J_SelectAll1 > div > label
        input2.send_keys(PSWD)
        submit.click()
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_MtSideMenu > div > dl:nth-child(1) > dd:nth-child(2) > a')))
        submit.click()
        all_handles = browser.window_handles
        search = browser.current_window_handle
        print(all_handles)
        for handle in all_handles:
            if handle!=search:
             browser.switch_to_window(handle)
        print(browser.page_source)
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SelectAll1')))
        submit.click()
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SmallSubmit')))
        submit.click()
        #J-security > div.ui-securitycore.ui-securitycore-tip.J-securitycoreTip > div > div.ui-form-explain
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submitOrder_1 > div.wrapper > a.go-btn')))
        submit.click()

        #payPassword_container > div > i:nth-child(1)

        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J-security > div.ui-securitycore.ui-securitycore-tip.J-securitycoreTip > div > div.J-checkResult.fn-hide')))
        input = wait.until(EC.presence_of_element_located((By.ID, 'payPassword_rsainput')))
        input.send_keys('xxxxxx')#密码输入

        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_authSubmit')))
        submit.click()
        return

        #payPassword_container > div
        input = wait.until(EC.presence_of_element_located((By.ID, '#payPassword_container > div > i:nth-child(2)')))
#payPassword_container > div > i:nth-child(2)
        input.send_keys("9")#J_SelectAll1 > div > label
      #  submit.click()


if __name__ == '__main__':
    logintaobao()
