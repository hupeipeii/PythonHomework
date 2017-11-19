# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:59:31 2017

@author: zyy
"""

"""
Q1：x = x + 1 与 x  += 1有什么差别？？？

可变对象会被就地修改（无修拷贝引用）， 
不可变对象则和 A = A + B 的结果一样（分配一个新对象）

可变类型：列表、字典
不可变类型：元组、字符串、数值
"""
#可变类型
x = 1.1
id(x) #1641111297096
x = x + 1
id(x) #1641111297144

x = 1.1
id(x) #1641111297216
x += 1.1
id(x) #1641111297240

#不可变类型
xlist = [1,2,3]
id(xlist) #1641112602824
xlist = xlist + [4]
id(xlist) #1641112636616

xlist = [1,2,3]
id(xlist) #1641112635784
xlist += [4]
id(xlist) #1641112635784

"""
Q2：对象相等。您认为type(a) == type(b)和type(a) is type(b)之间的不同是什么？
为什么会选择后者？函数isinstance()与这有什么关系？

== 是指对象的值相等， is是指对象的类型相同。
isinstance(obj,type)等价于判断一个对象的类型与已知的类型是否相同
"""
a = 1
b = 2
type(a) == type(b)
type(a) is type(b)
isinstance(a,int)  #减少函数调用的次数

"""
Q3：
输入一个2维矩阵
打印该矩阵
（提示：用list嵌套list来表示矩阵）
例:
输入：
1 0
2 3

输出：
1 0
2 3
"""
matrix = []
for i in range(2):
    tmp = []
    tmp = input('').split(' ')
    tmp = [int(x) for x in tmp]
    matrix.append(tmp)

for i in matrix:
    print('%d %d' % tuple(i))    
        
#也可以用下面这段程序打印     
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j],end=' ')
    print('\n',end='')
        
    


