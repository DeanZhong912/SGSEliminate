# SGSEliminate
---
## 三国杀消消乐台词脚本
春节活动，游卡又出微信小游戏了，把武将名，技能，台词做成消消乐了，还挺有创意，就台词的关卡有点恶心，卡了好几天了，于是今天就想写一个脚本自动实现，基本功能写出来，一些细节有所不足，如果有大佬看到可以帮忙改进改进。

## 设计思路
~~从三国杀安装包中"sgs412/assets/res/audio"目录中的skill，victory，dead三个文件中获取音频数据。调用腾讯云的音频识别ASR，将所有台词识别出来，形成台词数据集。~~
1. 直接爬取[三国杀WIKI](https://wiki.biligame.com/msgs/)获取数据
2. 手机连接电脑，调用adb命令，截图获取屏幕，选取问题区域进行截取。
3. 对截取的部分调用腾讯云文本识别功能OCR，将图片转成一行题目文本。
4. 对得到的题目文本，选取其中两个字组成笛卡尔乘积集合，遍历台词数据集，查找包含两个字组合的台词。组成台词候选，从台词候选集中选取字符全都在题目文本set的台词进行返回得到精确匹配。
5. 使用topK算法，对题目文本在台词库中进行模糊匹配。

## 使用方法(台词)
因为用到了腾讯云服务，所以需要注册腾讯云账户,用免费额度，开通ASR,OCR服务，将个人密钥存到CloudKey.txt文件中，并安装腾讯云的依赖包。
1. 运行下面命令，得到台词文本，运行爬虫脚本，从[三国杀WIKI](https://wiki.biligame.com/msgs/)获取台词，武将，技能等数据。
```
//python testTSR.py
python SpiderSGS.py
```

2. 运行下面命令，得到屏幕截图
```
python test.py
```

3. 运行下面命令，得到截图的目标区域，这里不同手机修改testOCR.py文件image_cut_save函数中的box的大小，调整截图区域
```
python getInput.py
```

4. 运行下面命令，得到题目文本
```
python testOCR.py
```

5. 运行下面命令，得到台词的精确解
```
python search.py
```

6. 运行下面命令，得到台词的模糊解
```
python search2.py
```
## 使用方法(武将)
1,2,3,4步同上，第5步运行下面命令，返回武将答案
```
python Wujiang.py
```
## 使用方法(道具关)
1,2,3,4步同上，第5步运行下面命令，返回武将答案
```
python Daoju.py
```

## 存在问题
语音文本的识别存在有些台词，拼音识别对了，但是字错了，如果有游卡官方的台词库，基本就很容易了。再有就是台词匹配的算法，虽然思路很简单勉强够用，但是我觉得肯定有有好的思路。
目前，已经可以基本实现得到答案的辅助功能，只是台词库中部分台词的拼音转换有误，导致一些台词不能输出，后续把台词人工校正后会上传到仓库，就省去语音识别这一步了。

最新一版，直接从[三国杀WIKI](https://wiki.biligame.com/msgs/)爬取数据，不用语音识别了，准确率有了很大提升。

