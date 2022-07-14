import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('./finalData/finalData.csv')
tagInfo = pd.read_csv("./finalData/tagInfo.csv")

data = data.dropna()

# 全部小写
data["skill"] = [text.lower() for text in data["skill"]]

train, test = train_test_split(data, train_size=0.90, test_size=0.10)

print(f"训练集长度: {len(train)}\n测试集长度: {len(test)}")
train = train.reset_index(drop=True)
test = test.reset_index(drop=True)
print(f"训练集预览：\n{train.head()}")

train_skill = list(train["skill"])
train_target = list(train["tag"])
test_skill = list(test["skill"])
test_target = list(test["tag"])

from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer()
X_train_vec = vec.fit_transform(train_skill)
X_test_vec = vec.transform(test_skill)

y_train_vec = train_target
y_test_vec = test_target

vec_result = pd.DataFrame(X_train_vec.toarray(), columns = vec.get_feature_names())
vec_result

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
mnb_vec = MultinomialNB()
mnb_vec.fit(X_train_vec,y_train_vec)
y_predict_vec = mnb_vec.predict(X_test_vec)
print(f"预测准确率为:{mnb_vec.score(X_test_vec,y_test_vec)}\n")
print(classification_report(y_test_vec,y_predict_vec))

print(f"类别参考标准:\n{tagInfo}\n")
test_index = np.random.randint(len(test_skill));
print(f"需要预测的 test_skill[{test_index}]: \n{test_skill[test_index]}\n")
wordbag = vec.transform([test_skill[test_index]])
print(f"预测信息转换为词袋为:\n{wordbag.toarray()[0]}\n")
print(f"预测信息的实际职位为: {test_target[test_index]}")
print(f"朴素贝叶斯模型预测的职位结果为: {mnb_vec.predict(wordbag)[0]}\n")
if test_target[test_index] == mnb_vec.predict(wordbag)[0]:
    print("模型预测准确")
else:
    print("模型预测不准确")

# 模型保存
with open('model/predict.pickle','wb') as f:
    pickle.dump(mnb_vec,f)
with open('model/wordbag.pickle','wb') as f:
    pickle.dump(vec,f)