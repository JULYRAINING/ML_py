#start
# -*- coding:utf-8 -*-

from PIL import Image,ImageDraw
from PIL import ImageFilter
import random,sys

path = r"E:/image/origin/"
img = Image.open(path + "origin.jpg")

##图像处理##
#转换为RGB图像
img = img.convert("RGB")              

#经过PIL自带filter处理
#模糊滤镜
imgfilted_b = img.filter(ImageFilter.BLUR)
#轮廓
imgfilted_c = img.filter(ImageFilter.CONTOUR)
#边界加强
imgfilted_ee = img.filter(ImageFilter.EDGE_ENHANCE)
#边界加强(阀值更 大)
imgfilted_ee_m = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
#浮雕滤镜
imgfilted_em = img.filter(ImageFilter.EMBOSS)                    
#边界滤镜
imgfilted_fe = img.filter(ImageFilter.FIND_EDGES)                                                
#平滑滤镜
imgfilted_sm = img.filter(ImageFilter.SMOOTH)
#平滑滤镜(阀值更大)
imgfilted_sm_m = img.filter(ImageFilter.SMOOTH_MORE)
#锐化滤镜
imgfilted_sh = img.filter(ImageFilter.SHARPEN)
#细节滤镜
imgfilted_d = img.filter(ImageFilter.DETAIL)

##组合使用filter
group_imgfilted = img.filter(ImageFilter.CONTOUR)
group_imgfilted = group_imgfilted.filter(ImageFilter.SMOOTH_MORE)

##图像保存##
imgfilted_b.save(path + "BLUR.jpg")
imgfilted_c.save(path + "CONTOUR.jpg")
imgfilted_ee.save(path + "EDGE_ENHANCE.jpg")
imgfilted_ee_m.save(path + "EDGE_ENHANCE_MORE.jpg")
imgfilted_em.save(path + "EMBOSS.jpg")
imgfilted_fe.save(path + "FIND_EDGES.jpg")                                
imgfilted_sm.save(path + "SMOOTH.jpg")
imgfilted_sm_m.save(path + "SMOOTH_MORE.jpg")
imgfilted_sh.save(path + "SHARPEN.jpg")
imgfilted_d.save(path + "DETAIL.jpg")
group_imgfilted.save(path + "group.jpg")

##图像显示##
imgfilted_b.show()
imgfilted_c.show()
imgfilted_ee.show()
imgfilted_ee_m.show()
imgfilted_em.show()
imgfilted_fe.show()                                
imgfilted_sm.show()
imgfilted_sm_m.show()
imgfilted_sh.show()
imgfilted_d.show()
group_imgfilted.show()
#end