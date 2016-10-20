#coding:utf-8
'''
Created on 2016年10月17日

@author: TF
'''

from sklearn.datasets.base import Bunch
from section2.word_split import readfile
import cPickle as pickle
import os


bunch = Bunch(target_name = [], label = [], filenames = [], contents = [])

#分词语料Bunch对象持久化文件路径
wordbag_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\train_set.dat'
#分词后分类语料库路径
seg_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_seg/'

catelist = os.listdir(seg_path)

bunch.target_name.extend(catelist)

for mydir in catelist:
    class_path = seg_path + mydir +'/'
    file_list = os.listdir(class_path)
    
    for file_path in file_list:
        fullname = class_path + file_path
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())

       
file_obj = open(wordbag_path, 'wb')
pickle.dump(bunch, file_obj)
file_obj.close()

print '构建文本对象结束'
