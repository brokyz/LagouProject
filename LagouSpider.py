from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


def login(url):
    # 启动chrome引擎
    driver = webdriver.Chrome()
    # 登录拉勾网账户
    # driver.get('https://passport.lagou.com/login/login.html')
    driver.get(url)
    # 等待25s让用户登录
    time.sleep(25)
    return driver


def spider(driver, search, page, filename):

    # 搜索职业信息
    driver.get('https://lagou.com')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#search_input").send_keys(search)
    driver.find_element(By.CSS_SELECTOR, "#search_input").send_keys(Keys.ENTER)
    time.sleep(2)

    driver.find_elements(
        By.CSS_SELECTOR, ".other-hot-city .city-wrapper .hot-city-name")[0].click()
    # 爬取最新数据
    time.sleep(2)
    # driver.find_elements(By.CSS_SELECTOR, ".wrapper .order a")[1].click()
    if(page == 0):
        pages = driver.find_elements(By.CSS_SELECTOR, ".pager_not_current")
        n = 0
        for i in pages:
            n += 1
            print(i.text)
        page = int(pages[n-1].text)
        print("page:", page)

    job_list = []
    money_list = []
    skill_list = []
    ink_list = []
    area_list = []
    jobDes_list = []
    inkDes_list = []
    time.sleep(1)
    index = 0
    for k in range(page):
        index += 1
        time.sleep(2)
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
         # 工作待遇
        jobDes = driver.find_elements(
            By.CSS_SELECTOR, ".li_b_r")
        for i in jobDes:
            jobDes_list.append(i.text)
            print("jobDes is : " + i.text)
        # 公司描述
        inkDes = driver.find_elements(
            By.CSS_SELECTOR, ".industry")
        for i in inkDes:
            inkDes_list.append(i.text)
            print("inkDes is : " + i.text)
        print(f"爬取 {search} 第{index}页完毕,进行下一页爬取,需要爬取{page}页")
        driver.find_element(By.CSS_SELECTOR, ".pager_next").click()

    pd_job = pd.DataFrame(job_list, columns=['job'])
    pd_money = pd.DataFrame(money_list, columns=['money'])
    pd_skill = pd.DataFrame(skill_list, columns=['skill'])
    pd_ink = pd.DataFrame(ink_list, columns=['ink'])
    pd_area = pd.DataFrame(area_list, columns=['area'])
    pd_jobDes = pd.DataFrame(jobDes_list, columns=['jobDes'])
    pd_inkDes = pd.DataFrame(inkDes_list, columns=['inkDes'])
    # pd.merge(pd_job,pd_money,pd_skill,pd_ink,pd_area,left_index=True, right_index=True)
    data = pd.concat([pd_job, pd_money, pd_skill, pd_ink,
                     pd_area, pd_jobDes, pd_inkDes], axis=1)
    # print(data)
    savePath = 'data/' + filename + '.csv'
    data.to_csv(savePath, encoding='utf_8_sig')
    print("爬取 "+search+" 完毕")


# search = '硬件开发'
# page = 0
# filename = '硬件开发'
# spider(search, page, filename)

searchClass = ['后端开发', '移动开发', '前端开发', '人工智能', '测试', '运维', 'DBA', '硬件开发']
driver = login('https://passport.lagou.com/login/login.html')
for i in searchClass:
    spider(driver, i, 0, i)
    time.sleep(60)
print('全部数据爬取完毕')
driver.quit()
# driver = login('https://passport.lagou.com/login/login.html')
# spider(driver, '移动开发', 0, '移动开发')