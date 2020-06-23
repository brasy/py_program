
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# for windows, python3 declarition will be ignore

#1. function reference
print('----1.function reference----')
from math import pi
radius = input('\nwhat is the circle radius? ')
print('the area of the circle is', float(radius)**2*pi)
print('the circumference of the circle is', 2*float(radius)*pi)


print('bool(''): ', bool(''))
a = abs
print('a=abs, a(-1)=', a(-1))



#2. define function
print('\n----2.define function----')
def my_func(param):
    if param ==0:
        pass
    
    if param >=0:
        return param
    else:
        return -param


print('my_func(-2) = ', my_func(-2))

def nop():
    pass



#3. params check
print('\n----3.params check----')
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('BAD OPERAND type')


'''print('my_func(-2) = ', my_func('str'))'''


#4. return tuple
print('\n----4.return tuple----')
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

print('move(100, 100, 60, math.pi/6) = ', move(100, 100, 60, math.pi / 6))


#5. parameter: position param, default param, variable param, keywords param
print('\n----5.kinds of params ----')

'1.position param'
def power1(x):
    return x*x
print('power1(x): ', power1(5))

'2.multi param'
def power2(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print('\npower2(x,n): ', power2(5,3))

'3.default param'
def power3(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print('\ndefault param\npower3(x,n=2) \npower3(5): ', power3(5))
print('power3(5,3): ', power3(5,3))

'a. bad default param, as default param must be invariability'
def add_end(L=[]):
    L.append('END')
    return L

print('\nadd_end():',add_end())
print('again  add_end():',add_end())

'b. default param use None or str as invariability'
def add_end_none(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

print('\nadd_end_none():',add_end_none())
print('again  add_end_none():',add_end_none())


'4.variable param *param, as a tuple'
def calc(nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
print('\n*variable param (*param)\nnums is tuple or list, calc([nums])', calc([1,2,3]))
print('nums is tuple or list, calc((nums))', calc([1,2,3]))

def calc_var(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
print('\nvariable param, calc_var(*nums)',calc_var(2,3,4))
print('\nvariable param with dulp param, calc_var(*nums)',calc_var(2,3,4,3))


'5.keywords params, **kw, as a dict'
print('\n*keywords params (**kw)')
def person(name, age, **kw):
    print('name:',name,'age:',age,'others:',kw)

person('mike', 12)
person('boob',13,city='beijing')
person('adam',14,gender='M',job='engineer')

extra={'city':'beijing','job':'engineer'}
person('jack',15,**extra)


'6.name keywords params(p1,p2..), (**kw)-->(*,p1,p2..), to check kw'
print('\n*name keywords params, (*(arg),p1,p2...)')
print('must have * before nameParam, when refer must enter name of nameParams')
def person2(name,age,*,city,job):
    print('name:',name,'age:',age,city,job)

person2('jack',24,city='beijing',job='engineer')

def person3(name,age,*arg,city,job):
    print('name:',name,'age:',age, arg, city, job)
person3('jack',25,'male',city='nanjing',job='painter')
person3('jack',25,city='nanjing',job='painter')


'7. combination argument,including mondatory argument,default argument,variable argument,keyword argument and name argument'
print('\ncombination argument: ')
def f1(a,b=0,*args,**kw):
    print('a=',a,'b=',b,'args=',args,'kw=',kw)

def f2(a,b=0,c=1,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1,2)
f1(1,2,'a','b')
f1(1,2,3,'b',x=90)
f2(1,2,d=4)
f2(1,2,d=4,x=0)
f2(1,2,d=4,x=None)

print('\ncombination argument with func(*args, **kw)')
args = (1, 2, 4)
kw = {'d': 9, 'x': '#'}
f1(*args,**kw)
f2(*args,**kw)
