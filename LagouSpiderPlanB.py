from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


def spider(search, page, filename):
    # 启动chrome引擎
    driver = webdriver.Chrome()
    # 登录拉勾网账户
    # driver.get('https://passport.lagou.com/login/login.html')
    driver.get('https://passport.lagou.com/login/login.html')
    time.sleep(25)
    # 搜索职业信息
    driver.find_element(By.CSS_SELECTOR, "#search_input").send_keys(search)
    driver.find_element(By.CSS_SELECTOR, "#search_input").send_keys(Keys.ENTER)
    time.sleep(1)
    # 全国信息
    driver.find_elements(By.CSS_SELECTOR, ".option__2xJt5")[0].click()
    time.sleep(3)
    # 最新发布
    driver.find_elements(By.CSS_SELECTOR, ".option__21bte")[1].click()
    job_list = []
    money_list = []
    skill_list = []
    ink_list = []
    area_list = []
    jobDes_list = []
    inkDes_list = []

    time.sleep(3)
    for k in range(page):
        time.sleep(1)
        print("获取信息")
        # 获取工作名
        job = driver.find_elements(
            By.CSS_SELECTOR, ".item__10RTO .p-top__1F7CL a")
        for i in job:
            job_list.append(i.text)
            print("job is : " + i.text)
        # 获取工资
        money = driver.find_elements(By.CSS_SELECTOR, ".item__10RTO .money__3Lkgq")
        for i in money:
            money_list.append(i.text)
            print("money is : " + i.text)
        # 获取技能需求
        skill = driver.find_elements(
            By.CSS_SELECTOR, ".item__10RTO .ir___QwEG")
        for i in skill:
            skill_list.append(i.text)
            print("skills is : " + i.text)
        # 获取公司名
        ink = driver.find_elements(By.CSS_SELECTOR, ".item__10RTO .company-name__2-SjF a")
        for i in ink:
            ink_list.append(i.text)
            print("inks is : " + i.text)
        # 获取位置
        # area = driver.find_elements(By.CSS_SELECTOR, ".list_item_top .position .p_top .position_link .add")
        # for i in area:
        #     area_list.append(i.text)
        #     print("area is : " + i.text)
        # 工作待遇
        jobDes = driver.find_elements(By.CSS_SELECTOR, ".item__10RTO .il__3lk85")
        for i in jobDes:
            jobDes_list.append(i.text)
            print("jobDes is : " + i.text)
        # 公司描述
        inkDes = driver.find_elements(By.CSS_SELECTOR, ".item__10RTO .industry__1HBkr")
        for i in inkDes:
            inkDes_list.append(i.text)
            print("inkDes is : " + i.text)
        print("下一页")
        driver.find_element(By.CSS_SELECTOR, ".lg-pagination-next").click()
    print("爬取完毕")
    pd_job = pd.DataFrame(job_list, columns=['job'])
    pd_money = pd.DataFrame(money_list, columns=['money'])
    pd_skill = pd.DataFrame(skill_list, columns=['skill'])
    pd_ink = pd.DataFrame(ink_list, columns=['ink'])
    # pd_area = pd.DataFrame(area_list, columns=['area'])
    pd_jobDes = pd.DataFrame(jobDes_list, columns=['jobDes'])
    pd_inkDes = pd.DataFrame(inkDes_list, columns=['inkDes'])
    # pd.merge(pd_job,pd_money,pd_skill,pd_ink,pd_area,left_index=True, right_index=True)
    data = pd.concat([pd_job, pd_money, pd_skill, pd_ink, pd_jobDes,pd_inkDes], axis=1)
    # print(data)
    filename = 'data/' + filename + '.csv'
    data.to_csv(filename, encoding='utf_8_sig')
    driver.quit()


search = '后端开发'
page = 30
filename = '后端开发'
spider(search, page, filename)
