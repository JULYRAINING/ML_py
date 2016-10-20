#coding:utf-8
'''
Created on 2016年10月17日

@author: TF
'''
import sys
import os
from sklearn.datasets.base import Bunch
import cPickle as pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from section2.word_split import readfile


reload(sys)
sys.setdefaultencoding("utf-8")

#读取Bunch对象

def readbunchobj(path):
    file_obj = open(path, 'rb')
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch

def writebunchobj(path, bunchobj):
    file_obj = open(path, 'wb')
    pickle.dump(bunchobj, file_obj)
    file_obj.close()
    
    
if __name__ == '__main__':
        

    stopword_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\baidu_stop_words.txt'
    
    stpwrdlst = readfile(stopword_path).splitlines()
    
    
    path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\train_set.dat'
    bunch = readbunchobj(path)
    
    tfidfspace = Bunch(target_name = bunch.target_name, label = bunch.label, filenames = bunch.filenames, tdm = [], vocabulary = {})
    
    
    
    
    vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df= 0.5)
    
    transformer = TfidfTransformer()
    
    tfidfspace.tdm = transformer.fit_transform(vectorizer.fit_transform(bunch.contents))
    
    tfidfspace.vocabulary = vectorizer.vocabulary
    
    space_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\tfidfspace.dat'
    
    writebunchobj(space_path, tfidfspace)
    
    print 'saved'