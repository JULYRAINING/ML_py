#coding:utf-8
'''
Created on 2016年10月26日

@author: TF
'''
import numpy as np
#1j 表示虚数
#a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
a = 100 * np.random.randn(512, 512)
U, s, V = np.linalg.svd(a, full_matrices=True)
print a.shape,  U.shape, s.shape, V.shape

print s