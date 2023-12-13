#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# return含有函数以外的其他参数，会是一层一层的栈，层数多了会报错
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

# 尾递归：return只有函数本身，在下一层时，会提前计算，永远只有一层
def fact_t(n):
    return fact_t_itr(n, 1)

def fact_t_itr(num, result):
    if num == 1:
        return result
    return fact_t_itr(num - 1, num * result)

# 去除前后空格
def trim(s):
    if isinstance(s, str):
        raise TypeError(f'必须传入str，当前类型是{type(s)}')
    if str(s).startswith(' '):
        return trim(s[1:])
    if str(s).endswith(' '):
        return trim(s[:-1])
    if not str(s).startswith(' ') and not str(s).endswith(' '):
        return s

if __name__ == '__main__':
    num = fact(10)
    print(f'num: {num}')

    num_t = fact_t(10)
    print(f'num: {num_t}')

    my_trim = trim('  hello  ,my young     lady      ')
    print(f'my_trim===={my_trim}====')
