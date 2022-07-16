# LagouProject

- 对[拉勾招聘](https://www.lagou.com/)进行IT类工作信息进行爬取.
- 对爬取信息进行数据预处理.
- 对数据进行分析和可视化.
- 根据用户所掌握的技能对用户进行工作推荐.

# 概述
## 爬虫部分

爬取模块的代码为[LagouSpider.py](https://github.com/brokyz/LagouProject/blob/main/src/LagouSpider.py)

使用`selenium`库进行数据爬取, 爬取下来的数据以`.csv`格式存于`data/spider`目录

| 爬取内容 | 描述           |
| -------- | -------------- |
| job      | 工作名称       |
| money    | 薪资情况       |
| skill    | 岗位需要的技能 |
| ink      | 公司名         |
| area     | 工作地点       |
| jobDes     | 工作描述       |
| inkDes     | 公司描述       |

## 预处理部分

预处理模块的代码为[dataProcessing.py](https://github.com/brokyz/LagouProject/blob/main/src/dataProcessing.py)

读取目录`data\spider`中的所有'.csv'数据, 对数据进行预处理, 将预处理结果保存于指定路径'data/processed'


## 使用

在使用前需要安装`selenium`和`pandas`，这两个包。

```
pip install selenium pandas
```

需要安装相应的浏览器和匹配的浏览器驱动，本程序使用了`chrome浏览器`，相应内核可以前往[ChromeDriver](https://chromedriver.chromium.org/downloads)下载对应的版本。

本程序的执行逻辑被封装成了函数`spider(search, page, filename)`:

- search: 需要搜索的职位信息内容
- page: 爬取的页数（1页有15条数据）
- filename: 保存数据的文件名

示例：爬取 java 职位信息的 20 页数据，将爬取到的数据保存在当前目录为 `java_data.csv`

```python
search = 'java'
page = 20
filename = 'java_data'
spider(search, page, filename)
```
