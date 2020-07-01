#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	1. decorator,在函数调用的前后打印出'begin call','end call'
'''

	print('---####---')
	def log_be(func):
	    @functools.wraps(func)
	    def wrapper(*arg,**kw):
	        print('begin call %s():'%func.__name__)
	        ret = func(*arg,**kw)
	        print('end call')
	        return ret
	    return wrapper
	
	@log_be
	def now4():
	    print('2020-6-29')
	    
print(now4.__name__)    
print(now4())


'''
2. decorator, 即支持带text,也支持无text的
'''

	print('----@@@@----')
	def log_any(text='call'):
	    def decorator(func):
	        @functools.wraps(func)
	        def wrapper(*arg,**kw):
	            print('%s %s'%(text,func.__name__))
	            return func(*arg,**kw)
	        return wrapper
	    if callable(text):
	        return decorator(text)
	    else:
	        return decorator
	
	@log_any
	def now5():
	    print('2020-6-29')
	    
	'print(now5.__name__)' 
	print(now5())
	print('----##----')
	@log_any("begin call")
	def now6():
	    print('2020-6-27')
	    
	print(now6.__name__)    
	print(now6())



