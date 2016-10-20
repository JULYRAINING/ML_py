#coding=utf-8
'''
Created on 2016年10月17日

@author: TF
'''
import sys
import os
from numpy import *

if __name__ =='__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    def file2matrix(path, delimiter):
        recordList = []
        fp = open(path, "rb")
        content = fp.read()
        fp.close()
        
        rowlist = content.splitlines()
        
        recordList = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
        
        return mat(recordList)
    
    root = "data"
    pathlist = os.listdir(root)
    for path in pathlist:
        recordmat = file2matrix(root + "/" + path, ' ')
        print recordmat
        print shape(recordmat)
        

