#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:18:46 2019

@author: rain
"""
import pandas as pd
# melt dataframe 当一个dataframe中出现day1 day2 day3 这种时，(多列变两列)
#可以转成两列，（一列标记第几天，一列标记value, wide to long

df_melt = pd.melt(df, id_vars = [col1, col2], var_name='week', 
                  value_name = 'value')  
#id_vars 是原dataframe中不需要变的， var_name是想合并的列合并出来的新的名字， value 新列的值
data = pd.read_csv('/Users/rain/Desktop/数据预处理/weather.csv')
cols = data.columns  #出现所有col name
data_melt = pd.melt(data, id_vars = ['id', 'year', 'month', 'element'], 
                    var_name = 'day', value_name = 'temp')


# 将dataframe其中一列拆成两列  （str）
#第一种方法:先split（每一行是list，里面有很多ele, 然后get到第0个ele）
split = df[col].str.split('_')  #第一种方法:先split（每一行是list，里面有很多ele, 然后get到第0个ele）
df[new_col] = split.str.get(0) 

#例子
df = pd.read_csv('/Users/rain/Desktop/数据预处理/survey_visited.csv')
# drop 某一列的nan
df = df.dropna(subset = ['dated'])
split = df.dated.str.split('-')
df['year'] = split.str.get(0)
#第二种方法：全部一起
df[['year', 'mon', 'day']] = df.dated.str.split('-', expand=True)   # expand 自动帮分开了，直接就是3列

# reset index
df_tidy.reset_index()  

#join
pd.merge(left = df1, right = df2, on = [col], how = 'inner')   # left_on, right_on 若不同名

# pivot table long to wide （两列变多列）
df_pivot = df.pivot_table(index = [col1, col2], columns = 'element', values = 'value') 
#data.pivot(index = 'City', columns = 'Category', values = 'Count')  # index 是行， column是哪一列变成column_name（变成列名



# 试将element 这一列里面的row（不同分类） 按它的名字变成新col， 底下的value是另外一列的value
#例子
data_pivot = data_melt.pivot_table(index =  ['id', 'year', 'month', 'day'], 
                                   columns = 'element', values = 'temp').reset_index()   #去掉了nan