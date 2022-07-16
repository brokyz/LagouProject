import pandas as pd
import numpy as np
import jieba
from collections import Counter 

da = pd.read_excel('./finalData/finalData.csv')

print(da['tag'].value_counts())

del da['Unnamed: 0']

print(da['city'].value_counts())

print(da.groupby("city")['year_wages'].describe().sort_values(ascending=False,by = 'mean'))

da.groupby("tag")['year_wages'].describe().sort_values(ascending=False,by = 'mean')

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open(r'stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords
 
#扩展jieba分词词库
# dict='fencibuchong.txt'
# jieba.load_userdict(dict)
 
# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()+ ['nan', '工程']
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr
 
done = []
# 将输出结果写入out.txt中]
da_job = [str(a) for a in da['job']]
for line in da_job:
    line_seg = seg_depart(line)
    done.append(line_seg)
da_skill = [str(a) for a in da['skill']]
for line in da_skill:
    line_seg = seg_depart(line)
    done.append(line_seg)
da_jobDesl = [str(a) for a in da['jobDes']]
for line in da_skill:
    line_seg = seg_depart(line)
    done.append(line_seg)
da_inkDes = [str(a) for a in da['inkDes']]
for line in da_skill:
    line_seg = seg_depart(line)
    done.append(line_seg)

words = []
for i in done:
    words.append(i.split())
spam_words = Counter()

for msg in words:
    spam_words.update(msg)
    
print(spam_words.most_common(50))

done_str = " ".join(done)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import cv2
images = cv2.imread('拉钩.png')

# images = np.array(Image.open("拉钩.png"))
wc = WordCloud(font_path = "白舟鲸海酔侯书体.ttf",collocations=False,background_color = "black",max_words = 5000,mask=images)

wc.generate(done_str)
# wc.to_file("IMJG.jpg") 
plt.imshow(wc) 
plt.axis("off") 
plt.show()

skill_str =[]
for i in da['skill']:
    skill_str.append(str(i))

job_str =[]
for i in da['job']:
    job_str.append(str(i))

jobDes_str =[]
for i in da['jobDes']:
    jobDes_str.append(str(i))

inkDes_str =[]
for i in da['inkDes']:
    inkDes_str.append(str(i))

skill_st = " ".join(skill_str)
inkDes_st= " ".join(inkDes_str)
jobDes_st= " ".join(jobDes_str)
job_st= " ".join(job_str)

key_word_job = input()
if key_word_job in done_str:
    index= []
    for i in spam_words.most_common():
        if i[0] == key_word_job:
            print('该关键词在全体关键词中占比：',100*i[1]/len(words),'%')
    if key_word_job in job_st:        
        for j in da['job']:
            if key_word_job in str(j):
                index.append(list(da['job']).index(j))
#                 print(da.iloc[[list(da['job']).index(j)]])
    elif key_word_job in jobDes_st:
        for j in da['jobDes']:
            if key_word_job in str(j):
                index.append(list(da['jobDes']).index(j))
#                 print(da.iloc[[list(da['jobDes']).index(j)]])
    elif key_word_job in inkDes_st:
        for j in da['inkDes']:
            if key_word_job in str(j):
                index.append(list(da['inkDes']).index(j))
#                 print(da.iloc[[list(da['inkDes']).index(j)]])
    elif key_word_job in skill_st:
        for j in da['skill']:
            if key_word_job in str(j):
                index.append(list(da['skill']).index(j))
#                 print(da.iloc[[list(da['skill']).index(j)]])
    new_index = list(set(index))
    for i in new_index:
        
        print(da.iloc[[i]])
    
else:
    print('您输入的词不在检所范围内')