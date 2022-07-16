from mimetypes import init
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle
import warnings
warnings.filterwarnings("ignore")


def fitModel(data, *tagInfo):
    # 用于存放模型
    models = []
    # 去除缺失值
    data = data.dropna()
    # 全部小写
    data["skill"] = [text.lower() for text in data["skill"]]
    # 以9：1划分训练集和测试集
    train, test = train_test_split(data, train_size=0.90, test_size=0.10)

    # print(f"训练集长度: {len(train)}\n测试集长度: {len(test)}")
    train = train.reset_index(drop=True)
    test = test.reset_index(drop=True)
    # print(f"训练集预览：\n{train.head()}")

    train_skill = list(train["skill"])
    train_target = list(train["tag"])
    test_skill = list(test["skill"])
    test_target = list(test["tag"])

    # 训练词袋模型
    vec = CountVectorizer()
    X_train_vec = vec.fit_transform(train_skill)
    X_test_vec = vec.transform(test_skill)

    y_train_vec = train_target
    y_test_vec = test_target
    models.append(vec)

    # vec_result = pd.DataFrame(X_train_vec.toarray(),
    #                           columns=vec.get_feature_names())
    # vec_result

    # 训练多项式朴素贝叶斯分类模型
    mnb_vec = MultinomialNB()
    mnb_vec.fit(X_train_vec, y_train_vec)
    # y_predict_vec = mnb_vec.predict(X_test_vec)
    print(f"预测准确率为:{mnb_vec.score(X_test_vec,y_test_vec)}\n")
    # print(classification_report(y_test_vec, y_predict_vec))
    models.append(mnb_vec)
    if(tagInfo):
        print(f"类别参考标准:\n{tagInfo}\n")
        test_index = np.random.randint(len(test_skill))
        print(f"需要预测的 test_skill[{test_index}]: \n{test_skill[test_index]}\n")
        wordbag = vec.transform([test_skill[test_index]])
        print(f"预测信息转换为词袋为:\n{wordbag.toarray()[0]}\n")
        print(f"预测信息的实际职位为: {test_target[test_index]}")
        print(f"朴素贝叶斯模型预测的职位结果为: {mnb_vec.predict(wordbag)[0]}\n")
        if test_target[test_index] == mnb_vec.predict(wordbag)[0]:
            print("模型预测准确")
        else:
            print("模型预测不准确")
    return models


def saveModel(models, savePath):
    print(f"模型保存于：{savePath}")
    # 模型保存
    predictPath = savePath + 'predict.pickle'
    wordbagPath = savePath + 'wordbag.pickle'
    with open(predictPath, 'wb') as f:
        pickle.dump(models[1], f)
    with open(wordbagPath, 'wb') as f:
        pickle.dump(models[0], f)



if __name__ == '__main__':
    data = pd.read_csv('../data/processed/finalData.csv')
    tagInfo = pd.read_csv("../data/processed/tagInfo.csv")
    models = fitModel(data)
    savePath = '../model/'
    saveModel(models, savePath)


