#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:HanaIKADA
# 
# 这是基于向量空间模型来进行的相似性检索
# 
########################################
import csv
import operator
import re
import math
import jieba
from collections import Counter

def participle(text):      #几乎移除所有非字母数字的符号
    words = []
    words = [x for x in jieba.cut(text) if len(x) >= 2]
    return words
def calLen(i,nlist):
    # result = 0
    # for line in nlist:
    #     for col in line[1:]:
    #         if col[0] == i:
    #             tmp = col[1]
    #             tmp *= tmp
    #             result += tmp
    # result = round(result**0.5,3) #指数 保留位数
    # return result    
    return vector_len[i]

def calwtq(q,t,nlist,totalbook):  #计算查询q中词项t的wtq
    tf = 0
    df = 1 #设该词最少在1个文档里出现。
    for term in q:
        if t.lower() == term.lower():
            tf += 1
    for line in nlist:
        if line[0].lower() == t.lower():
            df = len(line) - 1
            break
    if tf == 0:
        wtq =0
    else:
        wtq = (1 + math.log(tf,10)) * (math.log((totalbook+0.0)/df,10))
    result = round(wtq,3)
    return result
    
def calwtd(i,t,nlist): #计算文章i中词项t的wtd
    # tf = 0
    # for line in nlist:
    #     if line[0].lower() == t.lower():
    #         for j in line[1:]:
    #             if j[0] == i:
    #                 tf = j[1]
    tf = all_tf[i].get(t,0)
    if tf == 0:
        wtf = 0
    else:
        wtf = 1 + math.log(tf,10)
    result = round(wtf,3)
    return result
    
def cosinescore(q,mlist,nlist): #计算相似度
    q = participle(q)
    totalbook = len(mlist) 
    scores = [[0,i] for i in range(totalbook)]#分数-编号     
    Len = [0 for i in range(totalbook)]   
    for i in range(0,totalbook):
        Len[i] = calLen(i,nlist) #复杂度高 1/2
    for t in q:
        wtq = calwtq(q,t,nlist,totalbook) 
        for i in range(0,totalbook):
            wtd = calwtd(i,t,nlist) #复杂度高 2/2
            scores[i][0] += wtq*wtd  #按照课本，wtq也可设为1
    for i in range(0,totalbook):
        scores[i][0] = scores[i][0] / Len[i]
        scores[i][0] = round(scores[i][0],3)
    return scores


def m_run(your_content):


    # q = input("请输入你的查询:")
    # res = cosinescore(q,mlist,nlist)

    # res.sort(reverse=True)#从大到小
    # # print("这是结果评分:")
    # # print(res)
    # print("您要找的是不是:"+mlist[res[0][1]][0]+" <"+str(res[0][0])+">")
    # print("或者是这些:")
    # # for i in range(1,len(res)):
    # #     print(mlist[res[i][1]][0]+" <"+str(res[i][0])+">")
    # for i in range(1,10):
    #     print(mlist[res[i][1]][0]+" <"+str(res[i][0])+">")
         
         
    q = your_content
    res = cosinescore(q,mlist,nlist)
    res.sort(reverse=True)#从大到小
    m_send = []
    for i in range(0,100):    #只发送100条结果
        m_send.append(mlist[res[i][1]][0])
    return m_send
    
def m_run_name_link():
	return name_link


#载入各种文件------------------------------------------
mlist = []  #list是关键字 mlist读取csv
nlist = []  #存倒排索引 word bookid:freq
vector_len = {} #存文档向量长度 文档号：长度
all_tf = {} #存各文档的所有词项频率 文档号：all词项
myfile = csv.reader(open('m_data.csv',encoding='utf-8'))
for line in myfile:
    mlist.append(line)

myfile = csv.reader(open('inin.csv',encoding='utf-8'))
for line in myfile:
	nlist.append(line)

fr = open("vele",'r+',encoding='utf-8')
vector_len = eval(fr.read())   #读取的str转换为字典
fr = open("altf",'r+',encoding='utf-8')
all_tf = eval(fr.read())
fr.close()
#载入完毕----------------------------------------------
name_link = {} #名字：链接
for i in range(0,len(mlist)):
	name_link[mlist[i][0]] = mlist[i][-1]