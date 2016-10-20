#coding:utf-8
'''
Created on 2016年10月18日

@author: TF
'''
from section2.tf_idf import readbunchobj, writebunchobj
from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from section2.word_split import readfile

stopword_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\baidu_stop_words.txt'
    
stpwrdlst = readfile(stopword_path).splitlines()

path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\test_set.dat'
bunch = readbunchobj(path)

testspace = Bunch(target_name = bunch.target_name, label = bunch.label, filenames = bunch.filenames, tdm = [], vocabulary = {})

train_space_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\tfidfspace.dat'

trainbunch = readbunchobj(train_space_path)

vectorizer = TfidfVectorizer(stop_words=stpwrdlst, sublinear_tf=True, max_df= 0.5, vocabulary=trainbunch.vocabulary)

transformer = TfidfTransformer()
    
testspace.tdm = vectorizer.fit_transform(bunch.contents)

testspace.vocabulary = trainbunch.vocabulary

test_space_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\testspace.dat'

writebunchobj(test_space_path, testspace)

print '测试集词向量空间已保存'
    