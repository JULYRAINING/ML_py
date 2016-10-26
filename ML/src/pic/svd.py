#coding:utf-8
'''
Created on 2016年10月26日

@author: TF
'''
from PIL import Image
import numpy as np


def loadImage():
    # 读取小图片
    #im = Image.open(r"E:\image\ml_min.bmp")
    # 读取原图片
    im = Image.open(r"E:\image\ml.jpg")
    # 显示图片
    im.show() 
    width, height = im.size
    print width, height
    
  
    
    im = im.convert("L") 
   
    data = im.getdata()
    data = np.matrix(data)
    
    # 变换成512*512
    #小图
    #data = np.reshape(data,(100,100))
    #原图
    data = np.reshape(data,(width,height))
    u, s, v = np.linalg.svd(data, full_matrices = True)
    
    print data.shape, u.shape, s.shape, v.shape
    print s
    new_im = Image.fromarray(data)
    print new_im
    new_im = new_im.convert("L")
    new_im.save(r"E:\image\ml_bit.jpg")
    # 显示图片
    new_im.show()
loadImage()