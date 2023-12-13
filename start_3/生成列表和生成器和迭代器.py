#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
1.生成列表存储整个列表;生成器存储算法，取值的时候计算
2.生成列表写法是[...];生成器写法是(...)

可以直接作用于for循环的数据类型有以下几种：
1.集合数据类型，如list、tuple、dict、set、str等；
2.generator，包括生成器和带yield的generator function。
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
iter(X)可以把Iterable变成Iterator

总之:
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
'''

'''
生成列表
'''
L = []
for i in range(1, 11):
    L.append(i * i)
print(f"L 等于{L}")

# 等于上面
L1 = [x * x for x in  range(1, 11)]
print(f"L1等于{L1}")

# 可以加判断，if在后面代表筛选
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(f"L2等于{L2}")
# if 在前面是表达式的一部分 if 符合 = x*x 不符合 -x
L2_1 = [x * x if x % 2 == 0 else -x for x in range(1, 11)]
print(f"L2_1等于{L2_1}")

# 总之后面是for循环的语法，前面只要把for循环变量按需求拼接就行

# 可以有两层循环
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(f"L3等于{L3}")

#可以有多个参数，和for循环语法相同
dict1 = {"name": "zhangsan", "age": 25, "city": "beijinng"}
L4 = [m + "->" + str(n) for m,n in dict1.items()]
print(f"L4等于{L4}")

'''
生成器
最后抛出StopIteration错误表示无法继续返回下一个值了

生成器可以用next()取值；也可以用for取值，但要设置好break条件
'''
def fib(depth):
    n,a,b = 0,0,1
    while n < depth:
        yield b
        n = n + 1
        a, b = b, a+b
    return "done"

# 杨辉三角
def triangles():
    L = [0,1,0]
    while True:
        yield L[1: -1]
        L = [0] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [0]

'''
迭代器
'''
# 判断是不是迭代器
from collections.abc import Iterator
listIsItro = isinstance([x for x in range(0, 10)], Iterator)
genIsItro = isinstance((x for x in range(0, 10)), Iterator)
print(f'listIsItro: {listIsItro}, genIsItro: {genIsItro}')


if __name__ == '__main__':
    gen = fib(5)
    while True:
        try:
            print(next(gen))
        except StopIteration as e:
            break

    t = triangles()
    # for i in range(10):
    #     print(next(t))
    cnt = 0
    for tri in t:
        if cnt <= 5:
            print(tri)
            cnt = cnt + 1
        else:
            break



