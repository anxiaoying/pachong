from peewee import *

db = MySQLDatabase(host='47.100.20.184',
                   user='zp_data',
                   passwd='**************',
                   database='zp_data',
                   charset='utf8',
                   port=3306)



class School(Model):
    job_name = CharField()   #职位名称
    company = CharField()    #公司名称
    pay = CharField()        #薪资
    site = CharField()       #公司地址
    time = CharField()    #发布时间
    posi = CharField()       #职位信息
    class Meta:
        database = db

if __name__ == '__main__':
    School.create_table()
    # School.insert(job_name='职位名称', company='公司名称', pay='薪资', site='公司地址', time='发布时间', posi='职位信息').execute()





