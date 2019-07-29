# _*_ coding: utf-8 _*_
# @time     : 2019/6/4 23:25
# @Author   : ricky
# @Email    : ...
# @File     : produce_train_data.py

import os
def produce_train_data(input_file,out_file):
    """
    Arg:
    input_file: rating data
    out_file: output_file
    """
    if not os.path.exists(input_file):
        return
    record = {}
    linenum = 0
    score_threshold = 4.0
    fp = open(input_file)
    for line in fp:
        if linenum == 0 :
            linenum += 1
            continue
        item = line.strip().split(',')
        if len(item) < 4:
            continue
        userid,itemid,rating = item[0],item[1],item[2]
        if float(rating) < score_threshold:
            continue
        if userid not in record:
            record[userid] = []
        record[userid].append(itemid)
    fp.close()
    fw = open(out_file,'w+')
    for userid in record:
        fw.write(" ".join(record[userid])+'\n')
    fw.close()


if __name__ == '__main__':
    produce_train_data('../data/ratings.csv','../data/train.txt')
