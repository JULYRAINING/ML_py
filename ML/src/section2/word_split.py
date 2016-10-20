#coding:utf-8
'''
Created on 2016年10月17日

@author: TF
'''
import sys
import os
import jieba


def savefile(savepath, content):
    fp = open(savepath, 'wb')
    fp.write(content)
    print 'saving:' + savepath
    fp.close()
    
def readfile(path):
    fp = open(path, "rb")
    content = fp.read()
    fp.close()
    print 'reading:' + path
    return content


if __name__ =='__main__':  
    
    reload(sys)
    sys.setdefaultencoding("utf-8")
    
    
    #未分词语料库路径
    corpus_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\answer/'
    #分词后路径
    seg_path = r'E:\Tools\Python\ml\data\tc-corpus-answer\train_seg/'
    
    catelist = os.listdir(corpus_path)
    print catelist
    for mydir in catelist:
        class_path = corpus_path+mydir+'/'
        seg_dir = seg_path+mydir+'/'
        if not os.path.exists(seg_dir):
            os.makedirs(seg_dir)
        file_list = os.listdir(class_path)
        for file_path in file_list:
            fullname = class_path + file_path
            content = readfile(fullname).strip()
            content = content.replace('\r\n', '').strip()
            content_seg = jieba.cut(content)
            savefile(seg_dir+file_path, ' '.join(content_seg))
            
    print '中文分词结束'