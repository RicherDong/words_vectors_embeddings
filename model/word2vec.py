# -*- coding: utf-8 -*-
# @Time   : 2019/1/8 15:31
# @Author : Richer
# @File   : train.py
# 此文件用于训练词向量模型
# 直接使用已经分装好的word2vec

from gensim.models import word2vec
from words_vectors_embeddings.model.base import Base

class Word2VecTrain(Base):


    def main(self):
        print('使用word2vec api接口进行训练, start train...')
        '''
         sentences：可以是一个list，对于大语料集，建议使用BrownCorpus,Text8Corpus或lineSentence构建。
         size：是指特征向量的维度，默认为100。
         alpha: 是初始的学习速率，在训练过程中会线性地递减到min_alpha。
         window：窗口大小，表示当前词与预测词在一个句子中的最大距离是多少。
         min_count: 可以对字典做截断. 词频少于min_count次数的单词会被丢弃掉, 默认值为5。
         max_vocab_size: 设置词向量构建期间的RAM限制，设置成None则没有限制。
         sample: 高频词汇的随机降采样的配置阈值，默认为1e-3，范围是(0,1e-5)。
         seed：用于随机数发生器。与初始化词向量有关。
         workers：用于控制训练的并行数。
         min_alpha：学习率的最小值。
         sg： 用于设置训练算法，默认为0，对应CBOW算法；sg=1则采用skip-gram算法。
         hs: 如果为1则会采用hierarchica·softmax技巧。如果设置为0（默认），则使用negative sampling。
         negative: 如果>0,则会采用negativesampling，用于设置多少个noise words（一般是5-20）。
         cbow_mean: 如果为0，则采用上下文词向量的和，如果为1（default）则采用均值，只有使用CBOW的时候才起作用。
         hashfxn： hash函数来初始化权重，默认使用python的hash函数。
         iter： 迭代次数，默认为5。
         trim_rule： 用于设置词汇表的整理规则，指定那些单词要留下，哪些要被删除。可以设置为None（min_count会被使用）。
         sorted_vocab： 如果为1（默认），则在分配word index 的时候会先对单词基于频率降序排序。
         batch_words：每一批的传递给线程的单词的数量，默认为10000。
        '''
        model = word2vec.Word2Vec(self.data, size=150, window = 2, min_count=1,sg = 1,negative = 10)

        model.save(self.word2vec_model)
        print('模型训练完成...')

