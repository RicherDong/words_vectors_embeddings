# -*- coding: utf-8 -*-
# @Time   : 2019/1/8 17:04
# @Author : Richer
# @File   : base.py
from words_vectors_embeddings.get_sentences import GetSentences

class Base(object):
    def __init__(self):
        sObj = GetSentences()
        self.data = sObj.get_data()
        self.word2vec_model = 'ckpt/word2vec/word2vec.model'
        self.fasttext_model = 'ckpt/fasttext/fasttext.model'
        self.data_len()


    def data_len(self):
        lens = [len(words) for words in self.data]
        print('训练数据词总数:{}'.format(sum(lens)))




