import pandas as pd
import recommendClass as rec
import numpy as np
data = pd.read_csv("./finalData/finalData.csv")

def main():
    print("recommendJob.py")
    # backTenJobs("vue")
    backTenJobs()


def backTenJobs(*skill):
    if(not skill):
        skill = []
        skill.append(input("请输入您掌握的技能："))
    tag = rec.recommendTag(skill)
    print(tag)
    print(rec.recommend(skill))
    recommendTagData = data[data["tag"] == tag].reset_index()

    recommend_data = recommendTagData.iloc[np.random.choice(
        range(recommendTagData.shape[0]), 10)].reset_index(drop=True)
    print(recommend_data)

def backVip(*skill,num):
    if(not skill):
        skill = []
        skill.append(input("请输入您掌握的技能："))
    tag = rec.recommendTag(skill)
    print(tag)
    print(rec.recommend(skill))
    recommendTagData = data[data["tag"] == tag].reset_index()

    recommend_data = recommendTagData.iloc[np.random.choice(
        range(recommendTagData.shape[0]), num)].reset_index(drop=True)
    print(recommend_data)


main()