#coding=utf-8
'''
Created on 2016年10月17日

@author: TF
'''

import cPickle as pickle
from numpy import *

def file2matrix(path, delimiter):
    recordList = []
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    
    rowlist = content.splitlines()
    
    recordList = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
    
    return mat(recordList)




#存储对象
recordmat = file2matrix('data/data.data', ' ')

file_obj = open('data/data.dump', 'wb')

pickle.dump(recordmat, file_obj)

file_obj.close()
#读取对象
read_obj = open('data/data.dump', 'rb')
readmat = pickle.load(read_obj)
print readmat

