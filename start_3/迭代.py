#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

'''

#判断一个对象是否可以迭代
from collections.abc import Iterable
isinstance('abc', Iterable)

# 迭代对象
for i in [1,2,3,4,5]:
    print(i)

dict1 = {"name": "zhangsan", "age": 25, "city": "beijinng"}
# 迭代dict的key
for key in dict1.keys():
    print(f"dict key: {key}")

for val in dict1.values():
    print(f"dict value: {val}")

for key,val in dict1.items():
    print(f'dict key {key}, dict value {val}')

def findMinAndMax(L):
    if not isinstance(L, list):
        raise TypeError("传入list")
    min = None
    max = None
    # 传入[]根本不会进循环
    for i in L:
        if max is None or i > max:
            max = i
        if  min is None or i < min:
            min = i
    return min, max

if __name__ == '__main__':
    print(findMinAndMax([]))