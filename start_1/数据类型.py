#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
数据类型和变量
'''
d1 = 123
d2 = 100_000
d3 = -800

f1 = 3.14
f2 = -9.01
print(type(f2))

'''
字符串和编码
'''
# 获得编码
ord_a = ord("A")
print(ord_a)
print(f"获得的编码是： {ord_a}")
ord_chn_z = ord("中")
print(f"获得的编码是： {ord_chn_z}")
# 获得对应字符
chr_66 = chr(66)
chr_25991 = chr(25991)
print(f"获得的字符是： {chr_66}")
print(f"获得的字符是： {chr_25991}")
# 有16进制，转成字符
hexChn = '\u4e2d\u6587'
print(f"获得的字符是： {hexChn}")
# b''代表把字符串按ascii编码成字符，中文不在ascii里，所以会报错；要用.encode('utf-8')编码
# chn_bytes = b'中文'
chn_bytes = '中文'.encode('utf-8')
# 长度是6，说明一个中文占2个字符
print(f"词语的长度是： {len(chn_bytes)}")
'''
占位符 
%d 整数 %10d 代表不足10位补足10位 
%f 浮点 %.2f 代表保留两位小鼠
%s 整数
%x十六进制
当%本身是字符串符号时，用%%转义

f-string f"{a} 的语文成绩是{c}，超过本班{b:.2f}%的同学"
'''
print('%10d-0%d' % (5, 1))
print('%.2f' % 3.1415926)
print('Age:%s. Gender:%s' %(25, True))
print("%s 的语文成绩是 %d, 超过了本班 %.2f%%的同学" %('小明', 86, 61.45678))
a = "小明"
c = 86
b = 61.33222
# {b:.2f}代表b保留两位小数
d = f"{a} 的语文成绩是{c}，超过本班{b:.2f}%的同学 "
print(d)


