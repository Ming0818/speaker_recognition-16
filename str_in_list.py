# -*- coding: utf-8 -*-

def str_list(string):
    strok = string[:]
    strok = strok[:-2]
    strok = strok[2:]
    strok = strok.split("], [")
    s = len(strok[0].split(','))
    lt = [0]*len(strok)
    for i in range(len(strok)):
        lt[i] = [0]*s
    for i in range(len(strok)):
       for j in range(s):
           lt[i][j] = float(strok[i].split(', ')[j])
    return lt