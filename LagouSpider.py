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
    time.sleep(30)
    # 搜索职业信息
    driver.find_element(By.CSS_SELECTOR, "#search_input").send_keys(search)
    driver.find_element(By.CSS_SELECTOR, "#search_input").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, ".other-hot-city .city-wrapper .hot-city-name")[0].click()

    job_list = []
    money_list = []
    skill_list = []
    ink_list = []
    area_list = []
    time.sleep(1)
    for k in range(page):
        time.sleep(1)
        print("获取信息")
        # 获取工作名
        job = driver.find_elements(
            By.CSS_SELECTOR, ".list_item_top .position .p_top .position_link h3")
        for i in job:
            job_list.append(i.text)
            print("job is : " + i.text)
        # 获取工资
        money = driver.find_elements(By.CSS_SELECTOR, "span.money")
        for i in money:
            money_list.append(i.text)
            print("money is : " + i.text)
        # 获取技能需求
        skill = driver.find_elements(
            By.CSS_SELECTOR, ".item_con_list .con_list_item .list_item_bot .li_b_l")
        for i in skill:
            skill_list.append(i.text)
            print("skills is : " + i.text)
        # 获取公司名
        ink = driver.find_elements(By.CSS_SELECTOR, ".company_name>a")
        for i in ink:
            ink_list.append(i.text)
            print("inks is : " + i.text)
        # 获取位置
        area = driver.find_elements(
            By.CSS_SELECTOR, ".list_item_top .position .p_top .position_link .add")
        for i in area:
            area_list.append(i.text)
            print("area is : " + i.text)
        print("下一页")
        driver.find_element(By.CSS_SELECTOR, ".pager_next").click()

    pd_job = pd.DataFrame(job_list, columns=['job'])
    pd_money = pd.DataFrame(money_list, columns=['money'])
    pd_skill = pd.DataFrame(skill_list, columns=['skill'])
    pd_ink = pd.DataFrame(ink_list, columns=['ink'])
    pd_area = pd.DataFrame(area_list, columns=['area'])
    # pd.merge(pd_job,pd_money,pd_skill,pd_ink,pd_area,left_index=True, right_index=True)
    data = pd.concat([pd_job, pd_money, pd_skill, pd_ink, pd_area], axis=1)
    # print(data)
    filename = filename + '.csv'
    data.to_csv(filename, encoding='utf_8_sig')
    driver.quit()


search = 'web前端'
page = 30
filename = 'web前端拉勾全国'
spider(search, page, filename)
