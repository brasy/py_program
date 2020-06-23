#!/usr/bin/env python3
#-*-coding:utf-8 -*-


'1. higher-order function 一个函数接收另一个函数作为入参'
'变量指向函数,函数名也是变量'

print(abs(-10))
f=abs
print(f)

def add(x,y,f):
    return f(x)+f(y)

print(add(-2,-20,f))
