# -*- coding: utf-8 -*-
# @Time   : 2019/1/8 16:15
# @Author : Richer
# @File   : get_sentences.py

import os

class GetSentences(object):
    def __init__(self):
        base_path = os.getcwd()
        # self.words_file = base_path + '/words.txt'
        self.words_file = 'E:/python_program/words_vectors_embeddings/words.txt'

    def get_data(self):
        with open(self.words_file, 'r', encoding='utf-8') as rf:
            lines = rf.readlines()
            sentences = []
            for line in lines:
                if not line:
                    continue
                sentences.append([s for s in line.split(" ") if s != '\n'])
            return sentences