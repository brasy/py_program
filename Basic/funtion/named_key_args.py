#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Key_kw(**kw):
    print('  Name Scope')
    print('-------------')
    for name,score in kw.items():
        print('%6s %d'%(name,score))
    print()

Key_kw(adam=90,lisa=89,bart=97)
data={'adam':90,'lisa':89,'bart':97}
Key_kw(**data)

def name_key(name,*,gender,city='beijing',age):
    print('Personal Info')
    print('--------------')
    print('Name: %s' % name)
    print('Gender: %s' % gender)
    print('City: %s' % city)
    print('Age: %s'% age)
    print()

name_key('bob',gender='male',age=20)
name_key('lisa',gender='famale',city='shanghai',age=19)
