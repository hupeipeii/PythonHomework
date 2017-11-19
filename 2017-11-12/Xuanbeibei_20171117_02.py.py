# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:27:39 2017

@author: Administrator
"""
Q1:#例1
x=b=c=[1]   #将对象[1]的引用赋值给变量x,b,c
id(x)
id(b)
#x,b两者的id相同，代表的是对同一个对象的引用
x=x+[2]  #普通赋值，[2]是一个列表（可变类型的变量）
x
id(x)   #x的id发生改变，代表给x分配了一个新的对象
c    #c还是代表原来那个对象
b+=[2]   #增量赋值，[2]是一个列表（可变类型的变量）
b
id(b)   #b的id没有改变，代表b对应的对象没有改变，只是对象的数值属性发生了变化
c   #虽然并没有改变c的值，但是因为b改变了原来对象的属性，所以c的值也变成[1,2]了

#例2        
x=b=c=1
id(x)
id(b)
id(c)   #x,b,c的id 相同，代表的是同一个对象的引用
x=x+1   #普通赋值，1是一个整数（不可变类型的对象）
x
b
c
id(x)  #x的id发生改变，代表给x分配了一个新的对象
id(b)  #b的id没有改变
id(c)  #c的id没有改变
b+=1   #增量赋值，1是一个整数（不可变类型的对象）
b
c  #c还是代表原来的那个对象
id(b)  #b的id发生了改变，且和普通赋值后a的id相同
id(c)  #c的id没有改变，还是原来的id
例2与例1的区别在于，例2的3是一个整数（不可变类型的对象），
所以这里不管是普通赋值还是增量赋值，都会将一个新的对象的引
用赋值给变量。对于不可变类型的对象（队列、字典等），改变它
的时候，就需要考虑普通赋值与增量赋值的区别，一个会引入对象，
一个会改变原有对象的属性。对于不可变类型的对象（数值，元组），
则两种赋值没有区别，都会引入新的对象。
 
Q2: type(a)==type(b)比较的是数据对象的值，type(a) is type(b)
表示type(a)和type(b)是对象身份的比较。后者在运行时少一次查询，
所有会选择后者。isinstance(object, classinfo)是Python中
的一个内建函数，该函数接受一个类型对象的元组作为其参数，依次
判断object的数据类型是否是classinfo中的其中之一，若是则返回True，
否则返回False。
  

Q3:
matrix=[[1,0],[2,3]]
for i in matrix:
    print(i)
 
Q4:#!/usr/bin/env python

'makeTextFile.py-create text file'

import os
ls=os.linesep

#get filename
while True:

if os.path.exists(fname):
    print "ERROR:'%s'already exists" % fname
else:
    break

#get file content (text) lines
all=[]
print"\nEnter lines('.'by itself to quit).\n"

#loop untill user terminates input
while True:
    entry=raw_input('> ')
    if entry=='.':
        break
    else:
        all.append(entry)

#write lines to file with proper line-ending
fobj=open(fname,'w')
fobj.writelines(['%s%s'%(x,ls)for x in all])
fobj.close()
print'DONE!'

#!/usr/bin/env python

def displayNumType(num):
    print num,'is',
    if isinstance(num,(int,long,float,complex)):
        print 'a number of type:',type(num)._name_
    else:
        print 'not a number at all!'
        
displayNumType(-69)
matrix=[[1,0],
        [2,3]]
