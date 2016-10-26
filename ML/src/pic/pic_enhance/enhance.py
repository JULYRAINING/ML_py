#coding:utf-8
'''
Created on 2016年10月26日

@author: TF
'''
from PIL import Image
import numpy as np


def loadImage():
    
    # 读取原图片
    im = Image.open(r"E:\image\ml.jpg")
    # 显示图片
    im.show() 
   
     #图像增强40%
    imgbri=im.point(lambda i : i*1.4)
    imgbri.show()
    
loadImage()