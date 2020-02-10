import requests
import json
from selenium import webdriver
from time import sleep

def log_cookie():
    driver = webdriver.Firefox()
    driver.get('https://www.51job.com/')
    dl = driver.find_element_by_xpath("//span[@class='abut showLogin']").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('17716550759')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('xxxxxx')
    driver.find_element_by_xpath('//*[@id="login_btn"]').click()
    sleep(1)
    if driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a').text == '马可':
        print('登录成功')
        cookie = driver.get_cookies()
        with open('cookie.ini','w') as f:
            json.dump(cookie, f)
        print(driver.get_cookies())

    else:
        print('登录失败')

def user_data():
    session = requests.session()
    session.headers ={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
    }
    cookie_dict = dict()
    with open('cookie.ini','r') as f:
        cookie = json.load(f)
        for i in cookie:
            cookie_dict[i['name']] = i['value']
    r = session.get('https://i.51job.com/resume/standard_resume.php', cookies=cookie_dict)
    r.encoding = 'gbk'
    print(r.text)


if __name__ == '__main__':
    user_data()