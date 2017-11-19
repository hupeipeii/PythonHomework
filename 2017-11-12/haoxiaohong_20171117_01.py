# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:40:27 2017

@author: hong
"""
#1题
整型(不可变对象):
x1=1
x1=x1+1
id(x1)
y1=1
y1 +=1
id(y1)
浮点型(可变对象)：
x2=1.0
x2=x2+1
id(x2)
y2=1
y2 +=1
id(y2)

#2题
type(a) == type(b)的意思是：type(a)等于type(b),这是一个赋值运算,是对象值比较。
type(a) is type(b)的意思是：type(a)和type(b)是同一个函数，这是一个布尔运算，是对对象身份的比较。
我们用对象身份的比较来代替对象值的比较，这是一个更好的方案，可以更快捷，更方便的调用，尤其是当很多类似的代码遍布程序中时。
使用函数isinstance()可以让if语句更加方便，并且具有更好的可读性。

#3题
import numpy as np
p=np.array([[1,0],[2,3]])
print p

matrix=[[1,0],[2,3]]
for i in matrix:
    print (i)
input

#4题t'makeTextFile.py -- create text file'
import os
ls=os.linesep
while True:
    fname=raw_input('Eenter filename: ')
    if os.path.exists("fname"):
        print "ERROR: '%s' already exists" % fname
    else:
        break
all=[]
print "\nEnter lines('.' by itself to quit).\n"
while True:
    entry=raw_input('> ')
    if entry=='.':
        break
    else:
        all.append(entry)
fobj=open(fname, 'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'

'readTextFile.py -- read and display text file'
fname=raw_input('Eenter filename: ')
print
try:
    fobj=open("readTextFile.py",'r')
except IOError, e:
    print "*** file open error:",e
else:
    for eachLine in fobj:
        print eachLine,
    fobj.close()