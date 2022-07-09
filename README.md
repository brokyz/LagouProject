# LagouSpider

使用`selenium`库对[拉勾招聘](https://www.lagou.com/)进行工作信息爬取。



## 爬取内容

| 爬取内容 | 描述           |
| -------- | -------------- |
| job      | 工作名称       |
| money    | 薪资情况       |
| skill    | 岗位需要的技能 |
| ink      | 公司名         |
| area     | 工作地点       |



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



## 数据展示

![](https://pic.imgdb.cn/item/62c8de19f54cd3f9372b6491.jpg)