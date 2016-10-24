# coding=utf-8
from PIL import Image
import numpy as np
# import scipy

def loadImage():
    # 读取图片
    im = Image.open(r"E:\image\ml.jpg")

    # 显示图片
    im.show() 
    
    im = im.convert("L") 
    data = im.getdata()
    data = np.matrix(data)
    print data 
    # 变换成512*512
    data = np.reshape(data,(512,512))
    new_im = Image.fromarray(data)
    # 显示图片
    new_im.show()
    
loadImage()