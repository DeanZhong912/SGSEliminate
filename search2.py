import re
from collections import Counter
from heapq import nlargest
# 两种算法
# 过筛法，去掉问题中返回结果较多的字，留下
# TopK 找到台词集中包含题目字符最多个数的台词

# 台词文本路径
#DeadPath = './dead.txt'
#SkillPath1 = './skill1.txt'
#SkillPath2 = './skill2.txt'
#VictoryPath = './victory.txt'
TcPath="./台词.txt"

# 过筛法
frequentWords = {'为','的','以','之','我','你','他','而','一','又','了','不','也','其','已','如','在','此','无','有','得','何','可'}
# 不过筛
#frequentWords = {''}


# 获取文本下的台词
def getTaiciDB(path):
    taiciList = []
    file = open(path,"r")
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        taiciList.append(line)
    return taiciList

# 从字符串集合中找出包含特定字符集最多的字符个数的前K个字符串
def find_top_k(strings, charset, k):
    count = Counter()
    for string in strings:
        count[string] = sum(1 for c in string if c in charset)
    return nlargest(k, count, key=count.get)

# 搜索台词
def searchTaiCi(Question,TaiciDB,k):
    # 每个集合返回三个
    result = find_top_k(TaiciDB,Question,k)
    return result

# 遍历台词库搜索
def run(Question,path,k):
    TaiciDB = getTaiciDB(path)
    result = searchTaiCi(Question,TaiciDB,k)
    print(path+"----\nResult:")
    if result != []:
        print(result)
    else:
        print("No Matching in the "+Path)
    return result

# 读取问题
f = open("./res.txt", "r")
input = f.readline()
Question = list(input)
del Question[-1]
print("Question:")
#print(Question)
Qs = set(Question)
# 去掉Question中 频繁出现的字（查询搜索结果多的）
QuestionP = list(Qs-frequentWords)
#print(Qs)
#print(QuestionP)

# 运行搜索
#V = run(QuestionP,VictoryPath,2)
#D = run(QuestionP,DeadPath,2)
#S1 = run(QuestionP,SkillPath1,5)
#S2 = run(QuestionP,SkillPath2,5)

print("-----ALL RESULT-----")
#for bx in set(V+D+S1+S2):
#    print(bx)
run(QuestionP,TcPath,5)

