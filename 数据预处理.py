#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:40:37 2019

@author: rain
"""

# 查看这个dataframe的每一个col的missing data， 有多少个数据， 有多少个unique数据，以及其他的summary
# 在一开始要去确认 每一列的datatype, 建立两个list， 一个存连续性变量，一个存离散型变量
def summary(df):
    """
    return - 返回一个dataframe 其中包括：mean，std，分位数， missing data占比，数据总个数，每一列unique个数
    print - 是data info（包括数据类型）
    这个主要侧重的是连续型的变量
    """
    describe = df.describe()
    describe = describe.T
    total = len(df)
    describe['percentage of missing data'] = round((total - describe['count']) /total, 2)  #统计缺失值占比
    describe['count'] = total
    describe['number of unique'] = df.apply(lambda x: len(x.unique())) #应用在每一列上
    print (df.info())
    return (describe)
    
summary(data.drop(['race', 'sex','group']))

def summary(df):
    """
    return - 返回一个dataframe 其中包括: missing data占比，数据总个数，每一列unique个数, 最常出现的数据以及第二常出现的数据
    print - 是data info（包括数据类型）
    这个主要侧重的是离散型的变量
    """
    describe = df.describe()
    describe = describe.T
    total = len(df)
    describe['percentage of missing data'] = round((total - describe['count']) /total, 2)  #统计缺失值占比
    describe['count'] = total
    describe['number of unique'] = df.apply(lambda x: len(x.unique())) #应用在每一列上
    describe['mode'] = df.apply(lambda x: x.value_counts().idxmax())   #最frequent 是哪一个
    describe['mode_freq'] = df.apply(lambda x: x.value_counts().max()) # frequency是什么
    describe['mode_percentage'] = round(df.apply(lambda x: x.value_counts().max()/total), 2)
    describe['second_mode'] = df.apply(lambda x: x.value_counts().index[1])   #最frequent 是哪一个
    describe['second_mode_freq'] = df.apply(lambda x: x.value_counts()[1]) # frequency是什么
    describe['second_mode_percentage'] = round(df.apply(lambda x: x.value_counts().max()/total), 2)
    describe = describe[['count', 'number of unique', 'percentage of missing data', 'mode',
                         'mode_freq', 'mode_percentage', 'second_mode', 'second_mode_freq', 'second_mode_percentage']]
    print (df.info())
    return (describe)

summary(data[['race', 'sex','group']])


