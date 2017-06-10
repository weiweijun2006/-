import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import datetime  
import time
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
KEYWORD = 'xxx'
KEYWORD2 = 'xxxxx'
browser = webdriver.Chrome(service_args=SERVICE_ARGS)#PhantomJS
wait = WebDriverWait(browser, 10)

browser.set_window_size(1400, 900)
#buytime = '2016-12-27 22:31:00' 
def buy_on_time(buytime):
    now = datetime.datetime.now()
    print("准备抢票")
    print("现在时间：",now.strftime('%Y-%m-%d %H:%M:%S'),"\r抢票时间:",buytime)
    while True:
        now = datetime.datetime.now()

        if (now.strftime('%Y-%m-%d %H:%M:%S') == buytime):
            print("时间到")
            browser.refresh()
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SelectAll1')))
            submit.click()
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_SmallSubmit')))
            submit.click()
        #J-security > div.ui-securitycore.ui-securitycore-tip.J-securitycoreTip > div > div.ui-form-explain
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submitOrder_1 > div.wrapper > a.go-btn')))
            submit.click()
            
            
            #input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J-security > div.ui-securitycore.ui-securitycore-tip.J-securitycoreTip > div > div.J-checkResult.fn-hide')))
            input = wait.until(EC.presence_of_element_located((By.ID, 'payPassword_rsainput')))
            input.send_keys('xxxxxx')#密码输入

            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_authSubmit')))
            submit.click() 
            
            time.sleep(3)
            print (now.strftime('%Y-%m-%d %H:%M:%S'))
            print ('purchase success')
            return
        time.sleep(0.5)


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
        input.send_keys(KEYWORD)#J_SelectAll1 > div > label
        input2.send_keys(KEYWORD2)
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


        #payPassword_container > div > i:nth-child(1)


        return

        #payPassword_container > div
        input = wait.until(EC.presence_of_element_located((By.ID, '#payPassword_container > div > i:nth-child(2)')))
#payPassword_container > div > i:nth-child(2)
        input.send_keys("9")#J_SelectAll1 > div > label
      #  submit.click()


if __name__ == '__main__':
    logintaobao()
    buytime = '2017-06-10 16:26:00' 
    buy_on_time(buytime)
