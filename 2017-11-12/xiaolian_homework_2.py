# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:26:49 2017

@author: Lian Xiao
"""

'xiaolian_homework_2.py -- do my homework'

#Q1
可变对象：有区别。x+=没有改变对象的身份，改变了对象的值；
x=x+既改变了对象的身份又改变了对象的值。
y=x=[]
x+=[5]
'得到x=y=[5]'
x=x+[5]
'得到x=[5,5],y=[5]'
不可变对象：没有区别。
x=('s')
a=('b')
x=x+a
'得到x='sb',y='s''
x+=a
'得到x='sbb',y='s''

#Q2
type(a)==type(b)是对象值的比较
type(a) is type(b)是对象身份的比较
使用isinstance()可以让if语句更加方便，并且具有更好的可读性。

#Q3
print [[1,0],[2.3]]

#Q4
fname=raw_input('enter file name:')
all=[]
fobj=open(fname,'w')
fobj.writelines(['%s' % z for z in all])
fobj.close()
fobj=open(fname,'r')
for eachLine in fobj:
    print eachLine
    