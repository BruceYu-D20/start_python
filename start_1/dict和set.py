#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
dict和set：
1. 没有重复值
2. 无序
'''

'''
字典
1. key-value
2. 和list比较
  -> 查找和插入的速度极快，不会随着key的增加而变慢；
  -> 需要占用大量的内存，内存浪费多。
3. in判断元素在不在dict <Michael in d>
   或用get，d.get('Michael')
   get可以给默认值 d.get('jessey', 95)
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(f"dict是: {d}")
# 判断Michael是否在dict里
if_mic_in = 'Michael' in d
print(f'判断Michael是否在dict里：{if_mic_in}')
# 还可以用get
mic_score = d.get('Michael')
print(f'mic的成绩是{mic_score}')
jessey_score = d.get('jessey', 95)
print(f'jessey的成绩是{mic_score}')

'''
Set 无序和无重复元素的集合
创建set要传入一个list
'''
s = set([1, 2, 3])
s.add(4)
print(f"现在的set是：{s}")
s.remove(2)
print(f"现在的set是：{s}")
