#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer


# In[186]:


# 下面进行对Tokenizer的使用： 对word编译 可以是sequences 也可以是matrix
sentence = ['i love miaomiao',
           'i love tutu',
           'You love tutu, do you?']
tokenizer = Tokenizer(num_words = 100)  # num_words 最常使用的100个单词
tokenizer.fit_on_texts(sentence)
word_index = tokenizer.word_index   # dictionary
print (word_index)
sequences = tokenizer.texts_to_sequences(sentence)
print (sequences)
#test data 
test_sentence = ['i hate tutu',
                'you really love tutu!']
test_sequences = tokenizer.texts_to_sequences(test_sentence) #这种方式忽略了新单词
one_hot = tokenizer.texts_to_matrix(sentence, mode = 'binary')


# In[45]:


# 第二种方式： 添加oov,使新单词产生
tokenizer = Tokenizer(num_words = 100, oov_token = "<oov>")
tokenizer.fit_on_texts(sentence)
sequences = tokenizer.texts_to_sequences(sentence)
# test data
test_sentence = ['i hate tutu',
                'you really love tutu!']
test_sequences = tokenizer.texts_to_sequences(test_sentence)
print (test_sequences)
print (tokenizer.word_index)#有新单词的list


# In[41]:


# padding
from tensorflow.keras.preprocessing.sequence import pad_sequences
padded = pad_sequences(sequences, padding = 'post', truncating = 'post', maxlen = 4)  #把sequence转成矩阵  
#其中关键词：maxlen - 矩阵col长度， truncating - 跟着maxlen一起，=‘post’ 指的是从后截断, padding = 'post' 在后面加0 
print (padded)
# test
test_padded = pad_sequences(test_sequences)  #padding 只是把弄好的sequence 变成矩阵
print (test_padded)




# In[187]:


# enbedding
print (tf.__version__)
tf.enable_eager_execution()
get_ipython().system(' pip install -q tensorflow-datasets')
get_ipython().system(' pip install --ignore-installed protobuf==3.7')
import tensorflow_datasets as tfds
imdb, info = tfds.load('imdb_reviews', with_info = True, as_supervised = True)


# In[188]:


import numpy as np
train, test = imdb['train'], imdb['test']
train_sentences = []
train_labels = []
test_sentences =[]
test_labels = []
for s,l in train:
    train_sentences.append(str(s.numpy()))
    train_labels.append(l.numpy())
for s,l in test:
    test_sentences.append(str(s.numpy()))
    test_labels.append(l.numpy())
train_labels = np.array(train_labels)
test_labels = np.array(test_labels)


# In[190]:


# 超参数
vocab_size = 10000
embedding_dim = 16  #每一个被映射成了多少维
max_length = 120
trunc_type = 'post'
oov_tok = "<oov>"
# 开始啦
tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer.fit_on_texts(train_sentences)
sequences = tokenizer.texts_to_sequences(train_sentences)
padded = pad_sequences(sequences, maxlen = max_length, truncating = trunc_type)
word_index = tokenizer.word_index

test_sequences = tokenizer.texts_to_sequences(test_sentences)
#test_padded = pad_sequences(test_sequences, maxlen = max_length, truncating = trunc_type)
test_padded = pad_sequences(test_sequences, maxlen = max_length)


# In[193]:


# 超参数
vocab_size = 1000
embedding_dim = 16 
max_length = 120
trunc_type = 'post'
oov_tok = "<oov>"

# or just use matrix
# 开始啦
tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_tok)
tokenizer.fit_on_texts(train_sentences)
mat = tokenizer.texts_to_matrix(train_sentences, mode = 'binary')
test_mat = tokenizer.texts_to_matrix(test_sentences, mode = 'binary')


# In[197]:


# Embedding
from tensorflow.keras import Sequential
from tensorflow.keras import layers
model = Sequential()
model.add(layers.Embedding(vocab_size, embedding_dim, input_length = max_length)) 
#input_length在没有flatten 可以不要
model.add(layers.Flatten())  #拉成1维的
#model.add(layers.GlobalAveragePooling1D())
model.add(layers.Dense(6, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))
model.summary()


# In[198]:


model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
epoch = 10
model.fit(padded, train_labels, epochs = epoch, validation_data = (test_padded, test_labels))


# In[199]:


# matrix
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
epoch = 10
model.fit(mat, train_labels, epochs = epoch, validation_data = (test_mat, test_labels))


# In[159]:


# sarcasm
# 超参数
vocab_size = 10000   # 我们字典中的字数
embedding_dim = 16   # 每个字最后变成16维向量
max_length = 32      # 让sentences等长：每个sentence 32个字
trunc_type = 'post'
oov_tok = "<oov>"
padding_type = 'post'
train_size = 20000
#跑数据啦
import json
datastore = []
with open("sarcasm.json", "r") as f:
    for line in f:
        datastore.append(json.loads(line))
sentences = []
labels = []
urls = []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

# split data
train_sentences = sentences[:train_size]
train_labels = labels[:train_size]
test_sentences = sentences[train_size:]
test_labels = labels[train_size:]
    
tokenizer = Tokenizer(oov_token = oov_tok, num_words = vocab_size)
tokenizer.fit_on_texts(train_sentences)
train_sequences = tokenizer.texts_to_sequences(train_sentences)
padded = pad_sequences(train_sequences, padding = padding_type, truncating = trunc_type, maxlen =max_length)

test_sequences = tokenizer.texts_to_sequences(test_sentences)
test_padded = pad_sequences(test_sequences, padding = padding_type, truncating = trunc_type,maxlen =max_length)


# In[163]:


# 跑模型啦
model = Sequential()
model.add(layers.Embedding(vocab_size, embedding_dim, input_length = max_length))
#model.add(layers.Flatten())  
model.add(layers.GlobalAveragePooling1D())
model.add(layers.Dense(24, activation = 'relu'))
model.add(layers.Dense(1, activation = 'sigmoid'))
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
epoch = 10
histoty = model.fit(padded, train_labels, epochs = epoch, validation_data = (test_padded, test_labels))


# In[167]:


import matplotlib.pyplot as plt
acc = histoty.history['acc']
val_acc = history.history['val_acc']
epochs = range(epoch)
plt.plot(epochs, acc)
plt.plot(epochs, val_acc)
plt.ylabel('acc')
plt.legend(['acc','val_acc'])
plt.show()


# In[177]:





# In[ ]:




