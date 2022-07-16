import pickle
import pandas as pd
import re

def recommend(skill):
    skill = [i.lower() for i in skill]
    tagInfo =pd.read_csv("../data/processed/tagInfo.csv")
    with open('../model/predict.pickle','rb') as f:
        predict = pickle.load(f)
    with open('../model/wordbag.pickle','rb') as f:
        wordbag = pickle.load(f)

    word = wordbag.transform(skill)

    # print(word.toarray()[0])

    predict_tag = predict.predict(word)[0]

    predictJob = re.findall(re.compile(r'(.*).csv$'), tagInfo["class"][predict_tag])[0]   

    return predictJob

def recommendTag(skill):
    skill = [i.lower() for i in skill]
    # tagInfo =pd.read_csv("../data/processed/tagInfo.csv")
    with open('../model/predict.pickle','rb') as f:
        predict = pickle.load(f)
    with open('../model/wordbag.pickle','rb') as f:
        wordbag = pickle.load(f)

    word = wordbag.transform(skill)

    # print(word.toarray()[0])

    predict_tag = predict.predict(word)[0]

    # predictJob = re.findall(re.compile(r'(.*).csv$'), tagInfo["class"][predict_tag])[0]   

    return predict_tag


if __name__ == '__main__':
    pass
    # print("recommendClass.py")
    # skill1 = ["html css vue javascript"]
    # skill2 = ["springboot java mysql"]
    # skill3 = ["Android"]
    # print(f"{skill1} ===> {recommend(skill1)}")
    # print(f"{skill2} ===> {recommend(skill2)}")
    # print(f"{skill3} ===> {recommend(skill3)}")