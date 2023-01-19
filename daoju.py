from itertools import product
import re
Path1="./装备.txt"
Path2="./锦囊.txt"

def getDB(path):
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

def MatchCompose2Daoju(composes,daojus,Question):
    Match=[]
    for cp in composes:
        for name in daojus:
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

daojus = getDB(Path1)+getDB(Path2)
compose=getWordDKE(Question)
result=MatchCompose2Daoju(compose,daojus,Question)
print("Daoju:")
print(result)
