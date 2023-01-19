from itertools import product
import re

# 去除字符串中的标点
def removeBD(string):
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“”？，！【】（）、。：；’‘……￥·"""
    dicts={i:'' for i in punctuation}
    punc_table=str.maketrans(dicts)
    result = string.translate(punc_table)
    return result

# 求笛卡尔积
def getWordDKE(templist):
    compose = list(product(templist,templist))
    words = []
    for i in compose:
        if i[0]!=i[1]:
            word = i[0]+i[1]
            words.append(word)
    return words

# 获取文本下的台词
def getTaiciDB(path):
    taiciList = []
    file = open(path,"r")
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        taiciList.append(line)
    return taiciList

def get_strings_from_list(string_list, char_set):
    result = []
    for s in string_list:
        if all(c in char_set for c in s):
            result.append(s)
    return result

# 找到匹配的台词，看题目里面有没有对的上的字，没有就直接返回
def MatchWord2Taici(words,taicis,Question):
    MatchList = []
    for word in words:
        for taici in taicis:
            if re.match(word,taici) != None:
                #print(word)
                #print(taici)
                staici = removeBD(taici)#去掉标点
                MatchList.append(staici)
    
    Qset = set(Question)
    Result = get_strings_from_list(MatchList,Qset)
    
    return Result

# 读取问题
f = open("./res.txt", "r")
input = f.readline()
Question = list(removeBD(input))
del Question[-1]
print("Question:")
print(Question)

# 台词文本路径
DeadPath = './dead.txt'
SkillPath1 = './skill1.txt'
SkillPath2 = './skill2.txt'
VictoryPath = './victory.txt'

def run(Question,Path):
    # 得到问题的双字笛卡尔组合
    words = getWordDKE(Question)
#    print(len(words))
    
    # 读入台词文本
    taiciDB = getTaiciDB(Path)
#    print(len(taiciDB))

    # 进行匹配
    MatchResult = MatchWord2Taici(words,taiciDB,Question)

    print("-----\nResult:")
    if MatchResult != []:
        print(MatchResult)
    else:
        print("No Matching in the "+Path)
    
run(Question,VictoryPath)
run(Question,DeadPath)
run(Question,SkillPath1)
run(Question,SkillPath2)

