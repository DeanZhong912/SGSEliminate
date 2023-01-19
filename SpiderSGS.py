# 写一个简单的爬虫，从https://wiki.biligame.com/msgs/的API中获取台词数据

import requests
import urllib
import json
from bs4 import BeautifulSoup
import re
import time

# 直接从console中得到每一页的武将名数据,并保存到name.json中
# 从json文件中获取全部武将的名字
def getAllName():
    namepath = "./name.json"
    with open(namepath) as f:
        name = json.load(f)

    pagenameLst = name.values()

    nameLst = []
    for pagename in pagenameLst:
        for item in pagename:
            nameLst.append(item["*"])
    return nameLst

def getSoup(name):
    url = "https://wiki.biligame.com/msgs/"+name
    response = requests.get(url,'lxml')
    response.encoding='utf-8'
    html = response.text
    soup = BeautifulSoup(html,'lxml')
    return soup

# 爬取单页台词
def getTaiCiFromUrl(soup):
    templst = soup.find_all(name='div',attrs={"style":"align-self: center;"})
    taici = []
    for i in templst:
        if i.find_all(name='span',attrs={"class":"bikit-audio"})!=[]:
            tcs = str(i.text).split('/')
            taici.extend(tcs)

    taiciLst=list(set(taici))
    return taiciLst

# 爬取单页技能
def getSkillFromUrl(soup):
    # <span style="color: white" class="">武圣</span>
    templst = soup.find_all(name='span',attrs={"style":"color: white", "class":""})
    skills = []
    for i in templst:
        skills.append(i.text)
    skills=list(set(skills))
    return skills

def WriteIn(output,textLst):
    fout = open(output,'a')
    for text in textLst:
        fout.write(text+"\n")
    fout.close()

def buildJson(name,Skills,Taici):
    item ={}
    item["name"]=name
    item["skills"]=Skills
    item["taici"]=Taici
    return item

# 保存json文件
def SaveJson(dict_):
    with open("AllInfo.json", "a", encoding='utf-8') as f:
        # json.dump(dict_, f)  # 写为一行
        json.dump(dict_, f, indent=2, sort_keys=True, ensure_ascii=False)

# 保存台词到文本中
def Save():
    tcoutput = "./台词.txt"
    skoutput = "./技能.txt"
    nmoutput = "./武将.txt"
    number = 0
    nameLst = getAllName()
    WriteIn(nmoutput,nameLst)
    jsonDict = {}
    for name in nameLst:
        number+=1
        if number <=298:
            continue
        soup = getSoup(name)
        taiciLst = getTaiCiFromUrl(soup)
        skills = getSkillFromUrl(soup)
        result = buildJson(name,skills,taiciLst)
    
        WriteIn(tcoutput,taiciLst)
        WriteIn(skoutput,skills)
        jsonDict[number]=result
        print(number)
        print(name)
        time.sleep(3)
        
    SaveJson(jsonDict)
    

Save()
