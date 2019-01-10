# -*- coding: utf-8 -*-
# @Time   : 2019/1/8 16:46
# @Author : Richer
# @File   : test.py
import os
from gensim.models import word2vec
from gensim.models import FastText
from words_vectors_embeddings1.model.base import  Base

class Test(Base):
    def __init__(self, model):
        super(Test, self).__init__()
        self.model = model



    def main(self, sentence):
        if self.model == 'word2vec':
           model = word2vec.Word2Vec.load(self.word2vec_model)

        else:
           model = FastText.load(self.fasttext_model)

        print('词表长度：', len(model.wv.vocab))
        print('爱    对应的词向量为：', model['爱'])
        print('喜欢  对应的词向量为：', model['喜欢'])
        print('爱  和  喜欢的距离（余弦距离）', model.wv.similarity('爱', '喜欢'))
        print('爱  和  喜欢的距离（欧式距离）', model.wv.distance('爱', '喜欢'))
        print('与 爱 最相近的3个词：', model.wv.similar_by_word('爱', topn=3))
        print('与 喜欢 最相近的3个词：', model.wv.similar_by_word('喜欢', topn=3))
        print('爱，喜欢，恨 中最与众不同的是：', model.wv.doesnt_match(['爱', '喜欢', '恨']))


if __name__ == '__main__':
    arg = input()
    obj = Test('word2vec')
    obj.main(arg)
