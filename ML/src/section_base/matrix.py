#coding:utf-8
'''
Created on 2016年10月21日

@author: TF
'''
from scipy import linalg
import numpy as np

A = [[8,1,6], [3,5,7], [4,9,2]]
evals, evecs = linalg.eig(A)

print A

print np.linalg.inv(A)
print '特征值：', evals , "\n特征向量：", evecs

print 