# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 23:26:21 2017

@author: Administrator
"""
###########第一题，不太懂#################
x=1.0
print(id(x))
#174877216
x=x+1
print(x)
print(id(x))
#174877264
x=1.0
x+=1
print(x)
print(id(x))
y=1.0
print(id(y))
#174877120
y+=1
print(y)
print(id(y))
#174877192
################第二题###################
w=2.3
print(type(w))
id(type(w))# 506039824L
u='a'
print(type(u))
id(type(u))#506079328L

type(w)==type(u)#false
type(w) is type(u)#false
v=2.2
print(type(v))
id(type(v))#506039824L
'''
type(a)==type(b)是判断a b的对应的类型是否相同
type(a) is type(b)是判断type(a) 和 type(b)的id是否相同，即这两个变量是否指向同一个对象
'''
type(v)==type(w)#True
type(v) is type(w)#ture
##################################第三题###########################
'''
question：为什么两种方式访问矩阵中元素的方法会有差异？
'''
a=[[0, 1],
   [2, 3]]
print(a)
#访问矩阵中的元素
a[1][1]
a[0][0]


'''
载入numpy包，这个包是一个N维数组对象,可以用于对数组的运算
'''
import numpy

t=numpy.mat([[1,2],[3,4]])
print(t)
type(t)
t[1,1]#4
t[0,0]#1
print(t.shape)#获取矩阵的维度(2L, 2L)
############################第四题#######################
'''
'''
#!/usr/bin/env/python
'makeTextFile.py--create text file'
#介绍os模块
#https://www.cnblogs.com/kaituorensheng/archive/2013/03/18/2965766.html
#os模块是和文件，目录有关的
import os
ls =os.linesep
#get filename
while True:
    if os.path.exists('E:\code\python\a.py'):
        print "REEOR:'%s'already exists" % 'E:\code\python\a.py'
    else:
            break
        
        
        
        


