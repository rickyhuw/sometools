# _*_ coding: utf-8 _*_
# @time     : 2019/6/4 23:43
# @Author   : ricky
# @Email    : ...
# @File     : get_embedding.py
from gensim.models import word2vec
import os
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

def get_embedding(input_file,output_file):
    """
    train item embedding
    :param input_file:item_file
    :param output_file: embedding_file
    :return:
    """

    sentences = word2vec.Text8Corpus(input_file)

    # 训练模型，部分参数如下
    model = word2vec.Word2Vec(sentences, size=100, hs=1, min_count=1, window=3,iter=100,sg=1)
    # 计算某个词的相关词列表
    y2 = model.most_similar("27", topn=30)  # 10个最相关的
    print('和27相关的30个:\n')
    for item in y2:
        print(item[0], item[1])
    print("-------------------------------\n")
    print(model['1'])
    model.wv.save_word2vec_format(output_file,binary=False)

if __name__ == '__main__':
    get_embedding('../data/train.txt','../data/embedding_m.txt')