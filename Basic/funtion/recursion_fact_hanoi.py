#!/usr/bin/python3
#-*- coding:utf-8 -*-

# 1. recursion for factorials
def factorials(n):
    if n==1:
        return 1
    return n*factorials(n-1)

print('factorials(3): ',factorials(3))
print('factorials(12): ',factorials(12))

# tail recursion
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,pro):
    if num ==1:
        return pro
    return fact_iter(num-1,num*pro)

print('factorials(300): ',fact(300))
print('factorials(800): ',fact(800))



# 2. recursion for tower of hanoi
def move(n,a,b,c):
    if n==1:
        print('move', a, '->', c)
    else:
        print(n)
        move(n-1,a,c,b) #a->b
        print('--')
        move(1,a,b,c)   #last one a->c
        print('----')
        move(n-1,b,a,c) #b->c
        print('h',n)
        

move(1,'A','B','C')
move(2,'A','B','C')
move(3,'A','B','C')
