#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
practice： 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
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
