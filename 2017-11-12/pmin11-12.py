# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 14:16:11 2017

@author: dell
"""
xlist=[1,2,3]
id(list)
xlist=xlist+[4]
id(list)

xlist=[1,2,3]
id(list)
xlist +=[4]
id(list)

a=1
b=2
type(a)==type(b)
type(a) is type(b)
isinstance(a,int)

matrix=[]
for i in range(2):
    temp=[]
    temp=input('').split(' ')
    temp=[int(x) for x in temp]
    matrix.append(temp)
#打印1
for i in range(2):
    for j in range(2):
        print(matrix[i][j],end=' ')
    print()
#打印2
print('%d %d' %(matrix[0][0],matrix[0][1]))
for i in range(2):
    print('%d %d' %(tuple(matrix[i])))
