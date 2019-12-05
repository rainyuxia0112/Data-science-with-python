#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:38:45 2019

@author: rain
"""
#############################################################################  LOGISTIC 
import pandas as pd
data = pd.read_csv('Social_Network_Ads.csv')
import statsmodels.api

x = data[['Gender', 'Age', 'EstimatedSalary']]
Y = data['Purchased']
# pandas get dummy var
dummy = pd.get_dummies(x['Gender'])   #########

x = pd.concat((x[['Age', 'EstimatedSalary']], dummy[['Female']]), axis = 1) 
# add constant!
x = statsmodels.api.add_constant(x)   ##################### 

# split into training and validation data
import sklearn.model_selection
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, Y, train_size = 0.8)

# logistic regression
import statsmodels.formula.api as sm
model = sm.Logit(y_train, x_train)   # upper case
result = model.fit()   # 参数都在result里面
result.summary()   # 0.42


y_pre = result.predict(x_test)
def check(x):
    if x>=0.5:
        i = 1
    else:
        i = 0
    return (i)
y_pred = y_pre.map(check)

# confusion matrix   # used in prediction
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)


####################################################################  delete gender
x_del_gender = x.drop(['Female'], axis = 1)
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x_del_gender, Y, train_size = 0.8)


######## using same split
x_train = x_train.drop(['Female'], axis = 1)
x_test = x_test.drop(['Female'], axis = 1)


model2 = sm.Logit(y_train, x_train)
result = model2.fit()
result.summary()  # 0.44

y_pre = result.predict(x_test)
y_pred = y_pre.map(check)

# confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_pred)

###################################################################### Logistic 的R对照版本
import statsmodels.formula.api as sm
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv('Smarket.csv')
x = LabelEncoder()
encoder = x.fit_transform(data['Direction'])
data['Direction'] = encoder    

result = sm.logit(formula = 'Direction ~ Lag1 + Lag2 + Lag3 + Lag4 + Lag5 + Volume', data = data).fit()
result.summary()

# confusion matrix
result.pred_table()

# coeffcients
result.params

###################################################################### LDA


