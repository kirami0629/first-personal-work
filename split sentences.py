# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:08:46 2021

@author: 211814395卢雨祺
"""

import jieba

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

#对代码进行输出测试
#for i in range(14):
#    word, count = items[i]
#    print("{0:<5}{1:>5}".format(word, count))

#保存下分词成果    
f = open("split.txt","w",encoding='utf-8')
f.write(str(items))
f.close() 
