import requests
from selenium import webdriver
from time import sleep

def sy_text():
    driver = webdriver.Firefox()
    driver.get('https://www.51job.com/')
    dl = driver.find_element_by_xpath("//span[@class='abut showLogin']").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('17716550759')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('ying3690')
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    sleep(1)
    if driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a').text == '马可':
        print('登录成功')
        print(driver.get_cookie())

    else:
        print('登录失败')


if __name__ == '__main__':
    sy_text()