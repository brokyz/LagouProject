# LagouProject

- 对[拉勾招聘](https://www.lagou.com/)进行 IT 类工作信息进行爬取.
- 对爬取信息进行数据预处理.
- 对数据进行分析和可视化.
- 根据用户所掌握的技能对用户进行工作推荐.

## 概述

### 爬虫部分

爬取模块的代码为[LagouSpider.py](https://github.com/brokyz/LagouProject/blob/main/src/LagouSpider.py)

使用`selenium`库进行数据爬取, 爬取下来的数据以`.csv`格式存于`data/spider`目录

| 内容   | 描述           |
| ------ | -------------- |
| job    | 工作名称       |
| money  | 薪资情况       |
| skill  | 岗位需要的技能 |
| ink    | 公司名         |
| area   | 工作地点       |
| jobDes | 工作描述       |
| inkDes | 公司描述       |

### 预处理部分

预处理模块的代码为[dataProcessing.py](https://github.com/brokyz/LagouProject/blob/main/src/dataProcessing.py)

读取目录`data\spider`中的所有'.csv'数据, 对数据进行预处理, 将预处理结果保存于指定路径'data/processed'

| 内容        | 描述         |
| ----------- | ------------ |
| job         | 工作名称     |
| Low_wages   | 最低薪资(k)  |
| Hight_wages | 最高薪资(k)  |
| Year_wages  | 年薪(k)      |
| city        | 工作地点     |
| ink         | 公司名       |
| staff       | 公司员工数量 |
| JobDes      | 工作描述     |
| inkDes      | 公司描述     |

### 工作推荐部分

工作推荐使用了多项式朴素贝叶斯模型使用技能需求对工作类别进行预测, 模型训练源码[fitModel.py](https://github.com/brokyz/LagouProject/blob/main/src/fitModel.py), 训练模型保存于`model`目录下.

在[recommendClass.py](https://github.com/brokyz/LagouProject/blob/main/src/recommendClass.py)中, 对`model`目录中的模型进行调用, 对输入技能进行工作类别预测.

在[recommendJob.py](https://github.com/brokyz/LagouProject/blob/main/src/recommendJob.py)中调用了[recommendClass.py](https://github.com/brokyz/LagouProject/blob/main/src/recommendClass.py), 对用户所掌握的技能进行工作推荐.

## 使用

在使用前需要安装`selenium`, `pandas`, `numpy`.

```
pip install selenium pandas numpy
```

需要安装相应的浏览器和匹配的浏览器驱动，本程序使用了`chrome浏览器`，相应内核可以前往[ChromeDriver](https://chromedriver.chromium.org/downloads)下载对应的版本。

### [LagouSpider.py](https://github.com/brokyz/LagouProject/blob/main/src/LagouSpider.py)

- `login(url)`: 传入一个登录地址, 登录所需要的网页, 将返回一个登录后的浏览器对象.
- `spider(driver, search, page, savePath)`: 传入登录后的浏览器对象, 搜索内容, 爬取的总页数和爬取的数据保存的路径. search 为列表类型, page 为 0 时将默认爬取最大页数.

示例：

```python
searchClass = ['后端开发', '移动开发', '前端开发', '人工智能', '测试', '运维', 'DBA', '硬件开发']
page = 0
savePath = '../data/spider/'
driver = login('https://passport.lagou.com/login/login.html')
for i in searchClass:
    spider(driver, i, page, savePath)
    time.sleep(60)
print('全部数据爬取完毕')
driver.quit()
```

### [dataProcessing.py](https://github.com/brokyz/LagouProject/blob/main/src/dataProcessing.py)

- `process(dataPath, savePath)`: 传入需要预处理的数据所在路径和预处理完成数据所需要的保存路径.

示例:
```python
savePath = '../data/processed/finalData.csv'
dataPath = '../data/spider/'
process(dataPath, savePath)
```

### [fitModel.py](https://github.com/brokyz/LagouProject/blob/main/src/fitModel.py)

- `fitModel(data, *tagInfo)`: 传入预处理好的数据, 可选传入数据类别参照表. 如果传入参照表, 将对测试数据随机选取一个进行模型预测测试. 最后会以列表的形式返回拟合好的词袋模型和多项式朴素贝叶斯模型.

- `saveModel(models, savePath)`: 以列表的形式传入拟合好的模型, 和模型保存路径. 

示例:
```python
data = pd.read_csv('../data/processed/finalData.csv')
tagInfo = pd.read_csv("../data/processed/tagInfo.csv")
models = fitModel(data)
savePath = '../model/'
saveModel(models, savePath)
```

### [recommendClass.py](https://github.com/brokyz/LagouProject/blob/main/src/recommendClass.py)

- `recommend(skill)`: 以字符串形式传入已掌握的技能, 将返回推荐的类别名.
- `recommendTag(skill)`: 以字符串形式传入已掌握的技能, 将返回推荐的类别编号.

示例:
```python
skill1 = ["html css vue javascript"]
skill2 = ["springboot java mysql"]
skill3 = ["Android"]
print(f"{skill1} ===> {recommend(skill1)}")
print(f"{skill2} ===> {recommend(skill2)}")
print(f"{skill3} ===> {recommend(skill3)}")
```

### [recommendJob.py](https://github.com/brokyz/LagouProject/blob/main/src/recommendJob.py)

- `backTenJobs(*skill)`: 可选以字符串的形式传入技能, 将根据已掌握的技能推荐十个适合的工作. 如果不传入数据, 那么运行时将会让用户手动输入已掌握的技能.

示例:
```python
backTenjobs("html css vue javascript")
```



