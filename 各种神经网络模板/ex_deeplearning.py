#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:11:17 2019

@author: rain
"""

import pandas as pd
#### hand writing example
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

##############################  network building
import keras
from keras import models
from keras import layers
network = models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation='softmax'))
rms=keras.optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-06)    #先定义优化器，再放入
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy']
                )

#############################   put data into model
train_images=train_images.reshape((60000,28*28))
train_images=train_images.astype('float32')/255   # ?
test_images=test_images.reshape((10000,28*28))
test_images=test_images.astype('float32')/255 

#############################  preparing for labels
from keras.utils import to_categorical
train_labels=to_categorical(train_labels)    # 把label变成矩阵，一一对应model出来的值
test_labels=to_categorical(test_labels) 

network.fit(train_images,train_labels, epochs=7, batch_size=518)

########################### 放到测试集上
test_loss, test_acc= network.evaluate(test_images, test_labels)

########################### show the image
digit = train_images[5]
import matplotlib.pyplot as plt
from ipykernel.kernelapp import IPKernelApp
plt.imshow(digit)
