#!/usr/bin/env python3
#-*-coding:utf-8 -*-

'2. map(), reduce()'

def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7,8,9])
print(r)
print(list(r))


'''
字符串转整数,'13579'->13579
'''
'方法一：一个str2int函数'
from functools import reduce
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(char2num,s))

print(str2int('13579'))

'方法二： lambda函数化'
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('12468'))


'''
p1: 用户输入不规范英文名字，变成首字母大写，其它小写的规范名字
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
'''

def normalize(s):
    return s.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



'''
p2: Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积
'''
def quadrature(x,y):
    return x*y
def prod(L):
    def quadrature(x,y):
        return x*y
    return reduce(quadrature,L)

def prodLambda(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print('prodLambda: 3 * 5 * 7 * 8 =', prodLambda([3, 5, 7, 8]))


'''
p3: 利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456
'''

def str2float(s):
    flag=0
    def fn(x,y):
        nonlocal flag
        if flag == 0:
            if isinstance(x,(int,float)) & isinstance(y,int):
                return 10*x+y
            if isinstance(y,str):
                flag=1
                return x
        else:
            flag=flag*10
            return x+y/flag
        

    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'a'}[s]
    return reduce(fn,map(char2num,s))

print('str2float(\'123.456\') =', str2float('123.456'))

print('str2float(\'.456\') =', str2float('.456'))
print('str2float(\'0\') =', str2float('0'))
print('str2float(\'0.0456\') =', str2float('0.0456'))
print('str2float(\'123.45600\') =', str2float('123.45600'))

