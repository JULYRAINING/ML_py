#coding:utf-8
'''
Created on 2016年10月21日

@author: TF
'''
from numpy import *
from ID3Tree import *

dtree = ID3Tree()

dtree.loadDataSet('dataset.dat', ['age', 'revenue', 'student', 'credit'])
dtree.train()
print dtree.tree