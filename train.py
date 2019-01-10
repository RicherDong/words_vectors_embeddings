# -*- coding: utf-8 -*-
# @Time   : 2019/1/8 17:07
# @Author : Richer
# @File   : train.py

import sys
from words_vectors_embeddings.model.word2vec import Word2VecTrain
from words_vectors_embeddings.model.fasttext import FastTextTrain



def run(model):
    if model == 'word2vec':
        main = Word2VecTrain()
    else:
        main = FastTextTrain()
    main.main()



if __name__ == '__main__':
    # 可传入参数是 fasttext 或者是 word2vec  分别使用不同的词向量类型进行训练
    run('fasttext')

