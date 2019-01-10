# -*- coding: utf-8 -*-
# @Time   : 2019/1/8 17:09
# @Author : Richer
# @File   : fasttext.py

from words_vectors_embeddings.model.base import Base
from gensim.models import FastText

class FastTextTrain(Base):


    def main(self):
        print('使用fasttext 方式进行训练, start train...')

        model = FastText(sentences=self.data, sg= 1, size= 150, window =2, min_count=1)
        model.save(self.fasttext_model)

        print('模型训练完成...')
