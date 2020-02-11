import json
from time import sleep
import requests
from selenium import webdriver
from lxml import etree
from peewee_text import School
import datetime
def log_cookie():
    driver = webdriver.Firefox()
    driver.get('https://www.51job.com/')
    dl = driver.find_element_by_xpath("//span[@class='abut showLogin']").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('17716550759')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('*********')
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
    driver.close()
    driver.quit()


def intro(dz):          # 获取公司信息
    for i in dz:
        r = user_data(i)
        r.encoding = 'gbk'
        tree = etree.HTML(r.text)
        xpaths = tree.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/p/text()')  # 获取简介
        gs = tree.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[1]/a/p/text()') # 获取公司名称
        zw = tree.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/@title')     # 获取职位名称

        for i in zw:
            print(i)


def user_data(url):
    session = requests.session()
    session.headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    cookie_dict = dict()
    with open('cookie.ini','r') as f:
        cookie = json.load(f)
        for i in cookie:
            cookie_dict[i['name']] = i['value']
    r = session.get(url, cookies=cookie_dict)
    return r


def info_data():  # 获取信息地址，废弃原来首页获取信息！
    r = user_data('https://search.51job.com/list/010000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=')
    r.encoding = 'gbk'
    tree = etree.HTML(r.text)
    # xpaths = tree.xpath('//div[@class="el"]')
    # zw = tree.xpath( '//div[@class="el"]/p/span/a/@title')
    dz = tree.xpath( '//div[@class="el"]/p/span/a/@href' )
    # gs = tree.xpath( '//div[@class="el"]/span[@class="t2"]/a/text()')
    # dd = tree.xpath( '//div[@class="el"]/span[@class="t3"]/text()')
    # xz = tree.xpath( '//div[@class="el"]/span[@class="t4"]' )
    # sj = tree.xpath( '//div[@class="el"]/span[@class="t5"]/text()')
    intro(dz)

    # for i in range(len(zw)):
    #
    #     if xz[i].text != None:
    #         print('当前职位：%s，公司名称：%s,公司地址：%s,薪资：%s,发布时间%s'%(zw[i],gs[i],dd[i],xz[i].text,sj[i]))
    #         School.insert( job_name = zw[i], company = gs[i], pay = xz[i].text, site = dd[i], time = sj[i],
    #                        posi = '职位信息' ).execute()
    #     else:
    #
    #         print( '当前职位：%s，公司名称：%s,公司地址：%s,薪资：%s,发布时间%s' % (zw[i], gs[i], dd[i],'薪资未定', sj[i]) )
    #         School.insert( job_name = zw[i], company = gs[i], pay = '薪资未定', site = dd[i], time = sj[i],
    #                        posi = '职位信息' ).execute()




if __name__ == '__main__':
    # log_cookie()
    info_data()