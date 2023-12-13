#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
help(math.abs) 查看math.abs()的帮助
def 用于定义函数
pass在没想好写什么的时候，用于替代代码块
from abstest import my_abs：my_abs()的函数定义保存为abstest.py文件了，可以这么调用
isinstance() 用于检测参数类型
可变参数 def sum(*nums)，my_num=[1,2,3,4,5]，在调用时需要先把list tuple变成可变数据， sum(*my_num)会帮助我们把list变成可变参数
    sum()函数接受到的nums是一个tuple

要注意定义可变参数和关键字参数的语法：
    *args是可变参数，args接收的是一个tuple；
    **kw是关键字参数，kw接收的是一个dict。
    以及调用函数时如何传入可变参数和关键字参数的语法：
    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
    定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

def my_abs(x):
    # 用于判断类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        print(x)
    else:
        print(-x)

# n=4默认参数，如果不传入n=4
def power(x, n=4):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    sum = 1
    while n > 0:
        sum = sum * x
        n = n - 1
    return sum

# 关键字参数
# **kwargs的参数会放到dict里：Person('zhangsan', 30, city = 'beijing', school = 'tinghua') => {'city': 'beijing', 'school': 'tinghua'}
# 可以传入任何名字的关键字
def Person(name, age, **kwargs):
    print(f'name: {name} , age: {age} , other: {kwargs}')

# 可变关键字参数只能取名为city addr，传入其他关键字会报错：Person_addr() got an unexpected keyword argument 'school'
# *后面的参数被视为命名关键字参数
def Person_addr(name, age, *, city, addr):
    print(f'name: {name} , age: {age} , city: {city} , addr: {addr}')

# 定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 调用时，必须用city='....', school='....'的方式
def Person_addr_imummable(name, age, *scores, city, school = 'peking'):
    print(f'name: {name}, age: {age}, scores: {scores}, city: {city}, school: {school}')


# 可变参数，传入list时要用 my_sum(*list)把list变成可变参数
def my_sum(*nums):
    sum = 0
    for n in nums:
        sum = n + sum
    print(f'sum: {sum}')

if __name__ == '__main__':
    my_abs(-5)
    pow1 = power(2, 4)
    print(f'power(2,4): {pow1}')
    print(f'pow(2, 4): {pow(2, 4)}')
    # 可变参数
    my_num_list = [1,2,3,4,5]
    my_sum(*my_num_list)

    Person('zhangsan', 30, city = 'beijing', school = 'tinghua')
    Person_addr('zhangsan', 30, city = 'beijing', addr = 'haidian')

    Person_addr_imummable('zhangsan', 30, *[1,2,3,4,5], city='beijing')
