# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 03:10:43 2021

@author:211814395卢雨祺
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ### 1. 使用requests 获取网页源码

import requests
import re
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

### 准备工作
comment = []
comments= []
data='1613672133105'
cursor='0'

# ### 2. 使用正则表示式提取评论

for i in range(0,1268):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cursor+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_='+data
    source = requests.get(url, headers=headers).content.decode()
    comment= re.findall('content":"(.*?),"',source,re.S)
    comments.append(comment)
    cursor=re.findall('"last":"(.*?)"',source,re.S)[0].replace("\n","").replace(" ","")
    data=str(int(data)+1)
#print(comments)
    
# ### 3. 将提取评论保存
f = open("comments.json","w",encoding='utf-8')
f.write(str(comments))
f.close()
#print(comments)

