#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-25 23:16:24
# @Author  : jovi yang (jovi_yang@yeah.net)
"""
习题一：
1 用while语句的2种方法输出数字：1到10
2 用for语句和continue 输出结果：1 3 5 7 9
"""
x = 1
while x <= 10:
    print(x)
    x += 1
else:
    pass

a = []
for x in range(1, 10):
    if x % 2 == 0:
        continue
    else:
        a.append(x)
print(a)

'''
习题二：假设有列表
a = [1,2,3,4,5,6]
1 用for if else 的方法查找数字8是否在列表a里，如果在的话，输出字符串'find'，如果不存在的话，
输出字符串'not find'
2 用while语句操作上面的列表a，输出下面结果：
[2,3,4,5,6,7]
'''
a = [1, 2, 3, 8, 4, 5, 6]
for x in a:
    if 8 == x:
        print('Find')
    else:
        print('Not find.')

l = len(a)
x = 0
while x < l:
    a[x] += 1
    x += 1
else:
    pass
print(a)
