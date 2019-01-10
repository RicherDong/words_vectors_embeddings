# -*- coding: utf-8 -*-
# @Time   : 2019/1/7 15:32
# @Author : Richer
# @File   : word2vec_api.py

import os
import jieba
import re

article_path = os.getcwd() + '/data/'
article_file = article_path + 'demo.txt'
stop_words_file = article_path + 'stop_words.txt'

stopwords_set = set()
with open(stop_words_file, 'r', encoding='utf-8') as stop_words:
    for word in stop_words:
        stopwords_set.add(word.strip('\n'))

words = open('words.txt','w',encoding='utf-8')
with open(article_file, 'r') as file:
    for line in file:
        if not line or line == '\n':
            continue
        if re.match("http.*|……",line):
            continue
        line_sentence = ""
        line = line.strip("\n").strip()
        line_words = jieba.cut(line, cut_all = False)
        for new_word in line_words:
            if new_word not in stopwords_set and new_word:
                if new_word > u'\u4e00' and new_word <= u'\u9fa5':
                     words.write(new_word + " ")
                else:
                    break
        words.write("\n")
words.close()
