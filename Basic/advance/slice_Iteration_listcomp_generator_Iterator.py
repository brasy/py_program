#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'1. slice 切片'
print('-------- slice -------')
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

print('(1,2,3,4,5)[:3] = ',(1,2,3,4,5)[:3])
print('ABCDEF[:3] = ', 'ABCDEF'[:3])
print('ABCDEF[::2] = ', 'ABCDEF'[::2])


print('-------- Iteration -------')
'2. Iteration 迭代'
d={'a':1,'b':2,'c':3}
for key in d:
    print('key: ', key)
for v in d.values():
    print('value: ', v)
for key,v in d.items():
    print(key,':',v)

for strs in 'abcd':
    print(strs)


try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable
    
print('abc can Iterable:',isinstance('abc',Iterable))
print('1234 can Iterable:',isinstance(1234,Iterable))


for i,v in enumerate(['A','B','C']):
    print('enumerate() covert list to index-value: ',i,v)

for x,y in [(1,1),(2,4),(3,9)]:
    print('reference two parems: ', x,y)


'3. list comprehences 列表生成式'
print('------ list comprehences -------')

L1=[x*x for x in range(1,11)]
L2=[x*x for x in range(1,11) if x%2==0]
L3=[m+n for m in 'ABC' for n in '123']
print(L1,'\n',L2,'\n',L3)

import os
L4 = [d for d in os.listdir('.')]
print('os list dir: ', L4)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
L5 = [k + '=' + v for k, v in d.items()]
print('dict->list: ', L5)


L6 = ['Hello', 'World', 18, 'Apple', None]
L7 = [s.lower() for s in L6 if isinstance(s,str)]
print('filter lower from list: ', L7)



'4. generator 生成器'

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



'5. 迭代器'

from collections.abc import Iterable
from collections.abc import Iterator

print('isinstance([] is Iterable',isinstance([],Iterable))
print('isinstance([] is Iterator', isinstance([],Iterator))
print('isinstance(iter([]) is iterator',isinstance(iter([]), Iterator))

'for 实质上通过不断调用next()函数实现的'
for x in [1,2,3,4,5]:
    pass

it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
    except StopIteration:
        break

