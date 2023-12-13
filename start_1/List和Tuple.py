#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
'''

'''
List 可变：可删，可加，可按索引取数，最大索引是len(list - 1)，
增：append() insert(i, 加入的内容)
删除：pop() pop(i)
改：list[i] = 新内容
查：list[i]
'''
L1 = ['zhangsan', 'wangwu', 'zhaoliu']
print(f'现在的List是{L1}')
#删除末尾pop() pop(i)删除索引i的数据
L1.pop()
print(f'现在的List是{L1}')
# 加到list末尾
L1.append('Lisa')
print(f'现在的List是{L1}')
L1.pop(1)
print(f'现在的List是{L1}')
L1tail2 = L1[-2]
print(f'倒数第二个元素是{L1tail2}')
# 在1的位置上添加元素
L1.insert(1, "xiaoli")
print(f'现在的List是{L1}')


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

'''
tuple一旦初始化不可修改
增：不可修改
删：不可修改
改：不可修改
查：classmate[索引] 索引从0开始

注：() (1,) (1,2)都是元组，但(1)不是元组
'''
classmates = ('Michael', 'Bob', 'Tracy')
print(f"classmates的元组是： {classmates}")
michael = classmates[0]
print(f"访问第一个元素: {michael}")