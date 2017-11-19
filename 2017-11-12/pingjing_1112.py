#! usr/bin/env python
# -*- coding: utf-8 -*-

####  1题  ####
#while True:
#    variable = input('the type of varible (im/m): ')
#    model = int(input('choose "x = x + 1"(0) or "x += 1"(1): '))
#    if variable == 'im' :
#        immutable = 3.14      # 不可变对象实例
#        print(id(immutable))
#        if model:
#            immutable += 1
#        else:
#            immutable = immutable + 1
#        print(id(immutable))   # 两种模式下immutable的id都发生了变化
#    else:
#        mutable = [1, 2, 3]   # 可变对象
#        print(id(mutable))
#        if model:
#            mutable += ['test']
#        else:
#            mutable = mutable + ['test']
#        print(id(mutable))      # mutable的id没有发生变化
#    flag = input('continue or exit? (y/n):')
#    if flag == 'n':
#        break;
'''总结：可变对象允许值更新，不可变对象不允许值更新。
对于可变对象而言，“+”通过 __add__() 函数实现，而“+=”利用 __iadd()__ 函数实现'''


####  2题  ####
'''type(a) == type(b)和type(a) is type(b)之间的不同是什么？
为什么会选择后者？函数isinstance()与这有什么关系？'''

#解答
'''Python中的对象包含三要素：id、type、value。
其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值。
is判断的是a对象是否就是b对象，是通过id来判断的。
==判断的是a对象的值是否和b对象的值相等，是通过value来判断的。
isinstance()可以代替type比较，同时还可以实现某一变量对多个类型的比较，简化程序'''


####  3题  ####
#n = 2
#print('Input the number:')
#matrix = [[int(input()) for i in range(n)] for j in range(n)]
#for i in range(n):
#    for j in range(n):
#        print(matrix[i][j], end = ' ')
#    print('\n')
    
####  4题  ####
import os
ls=os.linesep
while True:
    fname= input('Eenter filename: ')
    if os.path.exists("fname"):
        print ("ERROR: '%s' already exists" % fname)
    else:
        break