#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'generator 生成器'

'斐波那契数列 1,1,2,3,5,8,13,21,34,...'

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'

def fibGenerator(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

'输出1'
for n in fibGenerator(6):
    print(n)

'输出2'
f1=fibGenerator(6)
while True:
    try:
        x=next(f1)
        print('f: ',x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break
