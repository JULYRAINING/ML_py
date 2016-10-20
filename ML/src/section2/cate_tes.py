#coding:utf-8
'''
Created on 2016年10月18日

@author: TF
'''
from sklearn.naive_bayes import MultinomialNB
from section2.tf_idf import readbunchobj

trainpath =  r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\tfidfspace.dat'
train_set = readbunchobj(trainpath)

testpath = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_word_bag\testspace.dat'
test_set = readbunchobj(testpath)

clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

predicted = clf.predict(test_set.tdm)

total = len(predicted)

rate = 0

for flabel, filename, expct_cate in zip(test_set.label, test_set.filenames, predicted):
    if flabel != expct_cate:
        rate +=1
        print filename, "：实际类别：",flabel, "-->预测类别：", expct_cate, 'failed'
    else:
        print filename, "：实际类别：",flabel, "-->预测类别：", expct_cate, 'success'

print 'error rate:' ,float(rate)*100/float(total), '%'