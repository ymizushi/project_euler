#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ファイルからテストデータ読み込み
def parse(filename):
    data = dict()
    with open(filename) as f:
        for line in f:
            data_set = line.strip('\n').split(' ')
            data[data_set[0]] = data_set[1].split(',')
    return data
test_data =  parse('test_data.txt')
s = map(lambda x: int(x), test_data.get('s'))
t = map(lambda x: int(x), test_data.get('t'))

def exclude_list(sublist, all_list):
    subset = set(sublist)
    allset = set(all_list)
    if subset.issubset(allset):
        return list(allset.difference(subset))
    else:
        return None

def exclude_list_list(sublist, all_list):
    return filter(lambda x: x != sublist, all_list)

all_st = range(min(s + t),max(s+t))
# print all_st
# print "intersetction", exclude_list([1,2,3,4], [1,2,3,4,5,6])

t_s = sorted(map(lambda x: range(x[0], x[1]), zip(s, t)), key=lambda x:len(x))
# print t_s

# len_t_s = map(lambda x: len(x), t_s)
# min_len = min(len_t_s)
# 
# print t_s
# print len_t_s

def calc(sublist, alllist, count):
    for sub in sublist:
        if set(sub).issubset(set(alllist)):
            # print sub,alllist
            return calc(exclude_list_list(sub, sublist), exclude_list(sub, alllist), count+1)
        else:
            continue
    return count
print calc(t_s, all_st, 0)
