import jenkins
import pymysql

jk = jenkins.Jenkins(url='http://localhost:8080/', username='aqin1012', password='941012')
# Jenkins的job数量
print(jk.jobs_count())
last_build_number = jk.get_job_info('aqin_test_01')['lastBuild']['number']
result = jk.get_build_console_output(name='aqin_test_01', number=last_build_number)
print(result)

# 数据筛选

# 数据入库
db = pymysql.connect(host="rm-bp1w54w01uzn79xx40o.mysql.rds.aliyuncs.com", user="appuser", password="Root1q2w",
                     database="db_ras")
user = result.split(' ')[3]
print(user)
cursor = db.cursor()
sql = "SELECT * FROM driver"
insert_sql = "INSERT INTO driver(uid,name,gender,phone,email,passwd,gmt_modify,gmt_create,delete_flag) " \
             "VALUES('" + user + "','aqin-driver','male','88888888','aqin@qq.com','password','2022-03-18 11:03:41','2022-03-18 11:03:41',0)"
try:
    execute = cursor.execute(insert_sql)
    print(execute)
    # 提交到数据库执行
    db.commit()
except IOError:
    # 如果发生错误则回滚
    print("except")
    db.rollback()
    # 关闭数据库连接
db.close()

