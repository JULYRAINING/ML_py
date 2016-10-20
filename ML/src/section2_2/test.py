#coding:utf-8
'''
Created on 2016年10月18日

@author: TF
'''
from section2_2.Nbayes import loadDataSet, NBayes

#加载训练集及分类标志
dataSet, listClasses = loadDataSet()
#实例化类
nb = NBayes()
#计算训练集相关参数
nb.train_set(dataSet, listClasses)
#将测试集映射到词向量模型
nb.map2vocab(dataSet[5])
#预测
print nb.predict(nb.testset)

print '完成'