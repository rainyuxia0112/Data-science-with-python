#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:00:30 2019

@author: rain
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding=utf-8
"""
Created on Tue Jul  9 20:32:15 2019

@author: rain
"""
# 利用 gensim similarity 与个人词库 对智慧领域打标签
## 导入包
import pandas as pd
from gensim.models import KeyedVectors
import gensim
import numpy as np
import pytz
import datetime

# 导入智慧领域标签
smart = pd.read_excel('./dictionary/Book2.xlsx', index_col=None)   # 导入智慧领域标签
name = list(smart.iloc[:,0])   # 智能领域的所有的名称
new_name = list(smart.iloc[:,1])[:-1] 
sim_name = [x[2:] for x in name[1:]]    # 去除智慧两个字带入模型

# 导入tencent 词向量 
model = KeyedVectors.load_word2vec_format('Tencent_AILab_ChineseEmbedding.txt',binary=False) 

# 导入自定义词库
absolute= pd.read_excel('./dictionary/absolute_classification.xlsx', index_col=None) 
absolute.words = absolute.words.map(lambda x: x.split(' '))


# 向model输入关键词， 输出与其最近的领域词，记录它的大小
def find_domain(keywords):
    '''
    keywords: type (list)
    return: 智能领域标签
    向model输入关键词， 输出与其最近的领域词，记录它的大小
    '''
    dic = {}
    for ele in keywords:
        try:
            l = []
            for na in sim_name:
                l.append(model.similarity(ele, na))
            key = name[l.index(max(l))+1]   # ele 对应的最大的领域词
            if key in dic.keys():
                dic[key] += 1          # 这个是不完美的，要改
            if key not in dic.keys():
                dic[key] = 1
        except:
            print (ele+'not in dcitionary')
    #for key in dic.keys():
        #dic[key] = np.mean(dic[key])
    if dic != {}:
        return (max(dic,key=dic.get))   
    else:
        return ('')

###################################################################################################### 贴智慧领域标签
def name_intelligent_field(data):
    '''
    对data进行智能领域填充
    return df: 包含文章id，title， keywords and intelligent_field
    '''    
    # 定义一个新列
    data['intelligent_field'] = ''
    
    # 开始对智能领域打标签：
    ## 如果领域名称 出现在标题了，直接打上领域名称 
    for i in range(len(data['title'])):
        for ele in sim_name:
            if data['title'].iloc[i].find(ele) != -1:
                data['intelligent_field'].iloc[i] = name[sim_name.index(ele)+1]
    ## 如果标题中有自定义词库的词，打上相应的领域标签                  
        for j in  range(len(absolute.words)):
            for k in absolute.words.iloc[j]:
                if data['title'].iloc[i].find(k) != -1:
                    if absolute.tag.iloc[j] not in data['intelligent_field'].iloc[i]: 
                        if  data['intelligent_field'].iloc[i] != '':
                            data['intelligent_field'].iloc[i] = data['intelligent_field'].iloc[i] + ',' + absolute.tag.iloc[j] 
                        else:
                            data['intelligent_field'].iloc[i] = absolute.tag.iloc[j] 
        print (i)
        
    # 用 函数find_domain 对剩余空白条目进行填充
    for i in range(len(data['title'])):
        if data['intelligent_field'].iloc[i] == '':
            data['intelligent_field'].iloc[i] = find_domain(data.keywords.iloc[i])
        print (i)
    
    df = data[['id', 'title', 'keywords' , 'intelligent_field']]
    
    return (df)
    
            
             


