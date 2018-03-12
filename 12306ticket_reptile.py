#-*- encoding:UTF-8 -*-
from splinter.browser import Browser
from time import sleep
import traceback

username = u"用户名"
passwd = u"密码"
#cookies nj--fy
starts = u"%u5357%u4EAC%2CNJH"
ends = u"%u961C%u9633%2CFYH"
# 时间格式2018-02-08
dtime = u"2018-02-08"
# 车次，选择第几趟，0则从上之下依次点击
order = 0
#设定乘客姓名
pa = u"乘客姓名"

#设定网址
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
#登录网站

def login():
    b.find_by_text(u"登录").click()
    sleep(3)
    b.fill("loginUserDTO.user_name", username)
    sleep(1)
    b.fill("userDTO.password", passwd)
    sleep(1)
    print u"等待验证码，自行输入..."
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break

#购票
def huoche(): 
    global b 
    b = Browser(driver_name="chrome")
    #返回购票页面
    b.visit(ticket_url) 

    while b.is_text_present(u"登录"): 
        sleep(1) 
        login() 
        if b.url == initmy_url: 
            break
    try:
        print u"购票页面..."
        b.visit(ticket_url)

        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()

        sleep(2)

        count = 0

        # 循环点击预订
        if order != 0:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count +=1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    b.find_by_text(u"预订")[order - 1].click()
                except:
                    print u"还没开始预订"
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                print u"循环点击查询... 第 %s 次" % count
                sleep(1)
                try:
                    for i in b.find_by_text(u"预订"):
                        i.click()
                except:
                    print u"还没开始预订"
                    continue
        sleep(1)
        b.find_by_text(pa)[1].click()
        print u"能做的都做了.....不再对浏览器进行任何操作"

    except Exception as e:
        print(traceback.print_exc())

if __name__ == "__main__": 
    huoche() 
