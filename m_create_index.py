#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HanaIKADA
# 
# 这是倒排索引的建立，同时存储了别的有利
# 于时间的数据
#####################################
import csv
import operator
import re
import math
import jieba
from collections import Counter

def participle(text):   #分词
    words = []
    words = [x for x in jieba.cut(text) if len(x) >= 2]
    return words
    
def getwith(j,text):  #返回text第j个词项
    if j < len(text):
        return text[j]
    return -1
  
def existw(n_dict,currword): #notexist,-1 else return loc
    return n_dict.get(currword,-1)


 
#建立倒排索引 -----------------------------------------------------
mlist = []  #list是关键字 mlist读取csv
nlist = []  #存倒排索引 word bookid:freq
n_dict = {} #用于索引倒排索引，存放关键词：文档号
vector_len = {} #存文档向量长度 文档号：长度
all_tf = {} #存各文档的所有词项频率 文档号：all词项

myfile = csv.reader(open('m_data.csv',encoding='utf-8'))
for line in myfile:
	mlist.append(line)
for i in range(0,len(mlist)):  #每一行数据
    text = ''
    for j in range(0,len(mlist[i])):
        text = text + mlist[i][j]
    text = participle(text)    #一行数据分词
    td = Counter(text)  #该文档中词项频率的dict
    all_tf[i] = td #存这个
    Vlen = 0
    value = td.values()
    for k in value:
        tmp = int(k)
        tmp = tmp*tmp
        Vlen = Vlen + tmp
    Vlen = round(Vlen**0.5,3)
    vector_len[i] = Vlen #存这个

    j = 0
    currword = getwith(j,text)
    j = j + 1
    while currword!=-1:#-1 == eof
        loc = existw(n_dict,currword)#notexist,-1 else return loc
        if loc == -1:
            tmp = []
            tmp.append(i)
            tmp.append(1)
            tmp1 = []
            tmp1.append(currword)#新词，补一行
            tmp1.append(tmp)
            nlist.append(tmp1)
            n_dict[currword] = len(n_dict) #有新词，更新倒排索引的索引
        else:
            if nlist[loc][-1][0] != i: #老词，但是新文档，加上去
                tmp = []
                tmp.append(i)
                tmp.append(1)
                nlist[loc].append(tmp)
            else:                      #老词，老文档，增加频数
                nlist[loc][-1][1]+=1
        currword = getwith(j,text)
        j = j + 1
#倒排索引建立完毕 -----------------------------------------------------

#倒排索引存盘
file = open("inin.csv",'a',encoding='utf-8',newline='')
w = csv.writer(file)
for i in range(0,len(nlist)):
    w.writerow(nlist[i])
file.close()

#vector_len存盘
fw = open("vele",'w+',encoding='utf-8')
fw.write(str(vector_len))      #把字典转化为str
fw.close()

#all_tf存盘
fw = open("altf",'w+',encoding='utf-8')
fw.write(str(all_tf))    
fw.close()