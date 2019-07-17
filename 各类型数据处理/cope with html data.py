#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:26:51 2019

@author: rain
"""

# 去除html格式
def remove_text(text, type='number'):
    """
    从文本中移除特定文本，例如数字或标点

    :param text: 文本
    :param type: 移除的文本类型, 可选'number', 'punc', 'both'
    :return: 移除后的文本
    """
    from zhon.hanzi import punctuation
    import string
    text = str(text)
    #text = re.sub("<>".format(punctuation, string.punctuation), " ", text)
    text = re.sub('<.*?>', '', text)
    text = re.sub('[.*?]', '', text)
    text = re.sub('([\w\-_]+(?:(?:\.|\s*\[dot\]\s*[A-Z\-_]+)+))([A-Z\-\.,@?^=%&amp;:/~\+#]*[A-Z\-\@?^=%&amp;/~\+#]){2,6}?', '', text)

    return text