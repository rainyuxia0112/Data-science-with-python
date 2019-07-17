#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:18:43 2019

@author: rain
"""
import pandas as pd
import json

### 清洗json格式数据

missing = []
id_ = []
tags = []
content = []
title = []
date = []
for i in range(len(data)): 
    try:
        title.append(json.loads(data.source.iloc[i])['title'])
        content.append(json.loads(data.source.iloc[i])['content'])
        id_.append(data.id.iloc[i])
        date.append(json.loads(data.source.iloc[i])['pubdate'])
        tags.append(json.loads(data.source.iloc[i])['tag'])
    except:
        try:
            title.append(json.loads(data.source.iloc[i] +'"}')['headline'])
            content.append(json.loads(data.source.iloc[i] +'"}')['content'])
            id_.append(data.id.iloc[i])
            date.append(json.loads(data.source.iloc[i]+'"}')['pubdate'])
            tags.append(json.loads(data.source.iloc[i]+'"}')['tag'])
        except:
            print (i)
            missing.append(i)

# 单独取出缺失值部分的数据
missing_data = data.loc[missing]
missing_data.to_excel('missing_data.xlsx')   

eigen_ch_old = pd.DataFrame({'id': id_, 'title':title, 'content':content, 'tag': tags, 'pubdate':date})   # 结束
# 去重
eigen_ch_new = eigen_ch_old.drop_duplicates(subset = 'title')   

