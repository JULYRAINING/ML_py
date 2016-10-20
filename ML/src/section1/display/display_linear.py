#coding=utf-8
'''
Created on 2016年10月17日

@author: TF
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
print x
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, yn, c = 'blue', marker = 'o')
ax.plot(x, y + 0.75, 'r')
plt.show()