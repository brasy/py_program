#!/usr/bin/env python3	
# -*- coding: utf-8 -*-
import math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs(-20)
print(n)
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


#ax2+bx+c=0
def quadratic(a,b,c):
    params = [a,b,c]
    length=len(params) - 1

    for n in params:
        if not isinstance(n,(int,float)):
            raise TypeError('bad operand type')
    print('----linear equation in two unkonwns----')

    if a==0:
        x1 = -c/b
        return x1
    
    factor = b**2-4*a*c

    if factor>0:
        x1 = (-b+math.sqrt(factor))/(2*a)
        x2 = (-b-math.sqrt(factor))/(2*a)
        return (x1,x2)
    if factor==0:
        x1=(-b)/(2*a)
        return x1
    if factor < 0:
        #raise TypeError('no real solution')
        pass

print(quadratic(2,0,1))
print(quadratic(0,2,1))
print(quadratic(2,3,1))
print(quadratic(1,3,-4))


    
       
