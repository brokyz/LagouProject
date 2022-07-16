import pandas as pd
import numpy as np
import re
import os


def main():
    savePath = '../data/processed/finalData.csv'
    dataPath = '../data/spider/'
    print(f"预处理开始，预处理数据路径为:{dataPath}")
    process(savePath, dataPath)


def process(savePath, dataPath):
    fileName = os.listdir(dataPath)
    print(f"读取到需要预处理的数据为:\n{fileName}\n共{len(fileName)}个文件")
    tag_info = pd.DataFrame(fileName, columns=['class'])
    
    tag_info["tag"] = tag_info.index
    tagPath = re.findall(re.compile(r'(.*)finalData.csv$'), savePath)[0] + 'tagInfo.csv'
    print(f"对数据进行分类:\n{tag_info}")

    # 读取数据
    n = 0
    creatVar = locals()
    dataList = []
    for i in fileName:
        path = dataPath + i
        creatVar["data" + str(i)] = pd.read_csv(path)
        creatVar["data" + str(i)]["tag"] = n
        dataList.append(creatVar["data" + str(i)])
        n += 1
    
    # 合并读取的数据数据
    data = pd.concat([dataList[0], dataList[1], dataList[2], dataList[3],
                      dataList[4], dataList[5], dataList[6], dataList[7]], axis=0)
    print("数据读取成功")
    data = data.dropna()
    data = data.reset_index()

    # 提取最高最低薪资
    # ^(\d\d?)k-(\d\d?)k
    hight_wages = np.array([])
    low_wages = np.array([])
    for i in data['money']:
        low_wages = np.append(low_wages, int(re.findall(
            re.compile(r'^(\d?\d?\d?)k-(\d?\d?\d?)k'), i)[0][0]))
        hight_wages = np.append(hight_wages, int(re.findall(
            re.compile(r'^(\d?\d?\d?)k-(\d?\d?\d?)k'), i)[0][1]))
    #     low_wages.append(int(re.findall(re.compile(r'^(\d?\d?\d?)k-(\d?\d?\d?)k'),i)[0][0]))
    #     hight_wages.append(int(re.findall(re.compile(r'^(\d?\d?\d?)k-(\d?\d?\d?)k'),i)[0][1]))
    year_wages = (hight_wages + low_wages) / 2 * 12
    hight_wages = hight_wages.tolist()
    low_wages = low_wages.tolist()
    year_wages = year_wages.tolist()

    # 提取城市信息
    # [\u4e00-\u9fa5]+
    city = []
    n = 0
    for i in data['area']:
        city.append(re.findall(re.compile(r'[\u4e00-\u9fa5]+'), i)[0])

    # 提取需要技能
    # [a-zA-Z]+
    skill = []
    for i in data['skill']:
        skill.append(",".join(re.findall(re.compile(r'[a-zA-Z]+'), i)))

    # 提取工作描述
    # [\u4e00-\u9fa5]+
    jobDes = []
    for i in data['jobDes']:
        jobDes.append(",".join(re.findall(re.compile(r'[\u4e00-\u9fa5]+'), i)))

    # 提取员工人数
    # (\d+)人
    staff = []
    for i in data['inkDes']:
        staff.append(",".join(re.findall(re.compile(r'(\d+)人'), i)))

    # 提取公司描述
    # (\w?[\u4e00-\u9fa5]+)
    tmp = []
    for i in data['inkDes']:
        tmp.append(
            ",".join(re.findall(re.compile(r'(.*)\s\d+[-]?\d+人以?上?'), i)))
    inkDes = []
    for i in tmp:
        inkDes.append(
            ",".join(re.findall(re.compile(r'(\w*[\u4e00-\u9fa5]+)'), i)))
    
    print("数据处理完毕")

    # 数据合并
    low_wages = pd.DataFrame(low_wages, columns=['low_wages'])
    hight_wages = pd.DataFrame(hight_wages, columns=['hight_wages'])
    year_wages = pd.DataFrame(year_wages, columns=['year_wages'])
    city = pd.DataFrame(city, columns=['city'])
    skill = pd.DataFrame(skill, columns=['skill'])
    jobDes = pd.DataFrame(jobDes, columns=['jobDes'])
    staff = pd.DataFrame(staff, columns=['staff'])
    inkDes = pd.DataFrame(inkDes, columns=['inkDes'])
    data2 = pd.concat([data['tag'], data['job'], low_wages, hight_wages,
                       year_wages, city, data['ink'], staff, skill, jobDes, inkDes], axis=1)
    print("数据合并完毕")
    data2.to_csv(savePath, encoding='utf_8_sig')
    tag_info.to_csv(tagPath, encoding='utf_8_sig')
    print("数据导出成功")
    print(f"数据导出到:{savePath}\n类别信息位于:{tagPath}")

main()
