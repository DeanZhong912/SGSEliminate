from itertools import product
import re
WujiangPath="./武将.txt"

def getWujiang(path):
    List = []
    file = open(path,"r")
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        List.append(line)
    return List

# 求笛卡尔积
def getWordDKE(templist):
    compose = list(product(templist,templist))
    words = []
    for i in compose:
        if i[0]!=i[1]:
            word = i[0]+i[1]
            words.append(word)
    return words

# 匹配组合和武将名
def MatchCompose2Wujiang(composes,wujiang,Question):
    Match=[]
    for cp in composes:
        for name in wujiang:
            if re.match(cp,name)!=None:
                Match.append(name)
    
    return Match


# 读取问题
f = open("./res.txt", "r")
input = f.readline()
Question = list(input)
del Question[-1]
print("Question:")
print(Question)

name=getWujiang(WujiangPath)
compose=getWordDKE(Question)
result=MatchCompose2Wujiang(compose,name,Question)
print("Wujiang:")
print(result)

