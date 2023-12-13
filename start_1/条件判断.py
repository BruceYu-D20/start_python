#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。

if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''

'''
匹配模式
match .. case
python 3.8 不支持

# 简单匹配
score = 'A'
match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _:
        print('score is ???.')
        
# 复杂匹配      
age = 15
match age:
    # 把age值给x
    case x if x < 10:
        print('< 10 years old.')
    case 10:
        print('10 years old.')
    # 多个值用 | 隔开    
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')

# 列表匹配
age = 15
match age:
    case x if x < 10:
        print('< 10 years old.')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')
'''



