#coding:utf-8
'''
Created on 2016年10月18日

@author: TF
'''

import numpy as np



def loadDataSet():
    postingList = [
        ['my', 'dog','has', 'flea', 'problems', 'help', 'please'], 
        ['maybe', 'not', 'take', 'him', 'to' 'dog', 'part', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him', 'my'],
        ['stop', 'posting', 'sutpid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how' 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
        ]
    classVec = [0,1,0,1,0,1]
    return postingList, classVec

class NBayes:
    
    def __init__(self):
        self.vocabulary =  []  #词向量
        self.idf= 0            #词语的IDF权值向量 大小：1*词语数量
        self.tf = 0            #词语频率矩阵              大小：训练集文件数*词语数量
        self.tdm = 0           #P（Xi/Yi） 后验概率
        self.Pcates = {}       #类别字典
        self.labels = []       #分类列表
        self.doclength = 0     #训练集文本数
        self.vocablen = 0      #词语数量
        self.testset = 0       #测试集
        
        
    def train_set(self, trainset, classVec):
        self.cate_prob(classVec)                                  #计算每个分类在数据集中的概率P（Yi）
        self.doclength = len(trainset)                            
        tempset = set()                                           
        [tempset.add(word) for doc in trainset for word in doc]   #生成词典
        self.vocabulary = list(tempset)                           
        self.vocablen = len(self.vocabulary)                      
        self.calc_wordfreq(trainset)                              #计算词频数据集
        self.build_tdm()                                          #按分类累计向量空间的每维值
        
    def cate_prob(self, classVec):
        '''
                        计算每个分类的概率P（Yi）
        '''
        self.labels = classVec
        labeltemps = set(self.labels)
        for labeltemp in labeltemps:
            #self.labels.count(labeltemp)
            self.Pcates[labeltemp] = float(self.labels.count(labeltemp))/float(len(self.labels))
            
    def calc_wordfreq(self, trainset):
        '''
                        计算IDF向量 和 TF矩阵
        '''
        self.idf = np.zeros([1, self.vocablen])
        self.tf = np.zeros([self.doclength, self.vocablen])
        for index in xrange(self.doclength):
            for word in trainset[index]:
                self.tf[index, self.vocabulary.index(word)] +=1
            for signleword in set(trainset[index]):
                self.idf[0, self.vocabulary.index(signleword)] += 1
                
    def build_tdm(self):
        '''
        
        '''
        self.tdm = np.zeros([len(self.Pcates), self.vocablen])
        sumlist = np.zeros([len(self.Pcates), 1])
        for index in xrange(self.doclength):
            self.tdm[self.labels[index]] += self.tf[index]
            sumlist[self.labels[index]] = np.sum(self.tdm[self.labels[index]])
        self.tdm = self.tdm/sumlist
        
    def map2vocab(self, testdata):
        self.testset = np.zeros([1, self.vocablen])
        for word in testdata:
            self.testset[0, self.vocabulary.index(word)] +=1
            
    def predict(self, testset):
        if np.shape(testset)[1] != self.vocablen:
            print 'demension mismatch'
            exit(0)
        
        predvalue = 0
        predclass = ''
        for tdm_vect, keyclass in zip(self.tdm, self.Pcates):
            temp = np.sum(testset*tdm_vect*self.Pcates[keyclass])
            print temp, predvalue
            if temp>predvalue:
                predvalue = temp
                predclass = keyclass
        return predclass
        
