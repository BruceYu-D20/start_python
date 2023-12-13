#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
截取 list tuple string 中的一部分
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取出0，1，2下标的数
L1 = L[0: 3]
print(f'取出0，1，2下标的数: {L1}')
# 取出前3个数
L1_1 = L[:3]
print(f'取出0，1，2下标的数: {L1_1}')
# 取出倒数第二和第三个数
L2 = L[-3: -1]
print(f'取出倒数第二和第三个数: {L2}')
# 取出末尾3个数
L2_2 = L[-3:]
print(f'取出倒数第二和第三个数: {L2_2}')

# tuple同list

# 字符串的截取
my_str = 'abcdefghijklmn'
start5_mystr = my_str[:5]
print(f'start5_mystr: {start5_mystr}')
