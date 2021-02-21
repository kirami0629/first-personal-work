# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:08:46 2021

@author: 211814395卢雨祺
"""

import jieba
import json

comments= open("comments.json", "r", encoding='utf-8').read()
    
 # 使用精确模式对文本进行分词
words = jieba.lcut(comments) 
    
 # 通过键值对的形式存储词语及其出现的次数
counts = {} 
    
for word in words:
    # 单个词语不计算在内
    if len(word) == 1: 
        continue   
    else: 
    # 遍历所有词语，每出现一次其对应的值加 1
        counts[word] = counts.get(word, 0) + 1 
          
# 将键值对转换成列表
items = list(counts.items())

# 根据词语出现的次数进行从大到小排序
items.sort(key=lambda x: x[1], reverse=True)

#print(items)

#对代码进行输出格式调整

List = []
for i in range(len(items)):
    Dict = {}
    word, count = items[i]
    if count >= 10:
        Dict['name'] = word
        Dict['value'] = count
        List.append(Dict)
# print(List)
        
#用json保存分词成果   
data = {}
data['value'] = List

f = open("split.json","w",encoding='utf-8')
f.write(str(items))
f.close() 