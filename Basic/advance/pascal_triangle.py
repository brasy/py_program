#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'5. 杨辉三角'

'''
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
...
'''
'''
期待输出
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
...
'''

def triangles1():
    n,a,b = 0,1,1
    L1 = [a]
    L2 = [a,b]
    L3 = [a,a+b,a]
    L4 = [a, a+(a+b),(a+b)+a,a]
    L5 = [a, a+(a+(a+b)),(a+(a+b)+(a+b)+a),(a+b)+a+a,a]
    print(L1,L2,L3,L4,L5)

def triangles2(L):
    if not isinstance(L,list):
        raise TypeError('bad type')
    for n,e in enumerate(L):
        if not isinstance(e,(int,float)):
            raise TypeError('bad operand type')
        if(n==0):
            print (L[n])
        elif(L[n]>=1):
            print (L[n]+L[n-1])
    print(1)   

L=[1,1]
triangles2(L)

def triangles():
    L=[1]
    while len(L)<10:
        print(L)
        L=[1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1]



''''输出1'
for n in triangles():
    print(n)
    n = n+1
    if n == 10:
        break

'输出2'
f1=triangles()
while True:
    try:
        x=next(f1)
        print('f: ',x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break
'''
