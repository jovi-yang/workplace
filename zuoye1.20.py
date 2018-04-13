#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 22:38:00
# @Author  : jovi yang (jovi_yang@yeah.net)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$


def max_num(a, b, c):
    '返回三个数字中最大的那个数字'
    x = max(a, b, c)
    return x


x = max_num(123, 345, 444)
print(x)
print(max_num.__doc__)


# 2 分别写2个函数，完成下面的功能：
# 提示一下用到函数的：**和*，猩猩是字典，星是元组
# 2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果：
# [22, 44, 88]
# 2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：
# ('xaay','yaay','zaay')


def ainfo(*arguments):
    '''
    2.1 调用函数：ainfo(x=88,y=22,z=44) 你定义ainfo函数体里面的内容并且返回结果：
    [22, 44, 88]
    '''
    t = [x for x in arguments]
    t.sort()
    return t


l = ainfo(88, 22, 44)
print(l)


def cinfo(**keywords):
    '''
    2.2 调用函数：cinfo(x=88,y=22,z=44) 你定义cinfo函数体里面的内容并且返回结果：
     ('xaay','yaay','zaay')
    '''
    t = tuple([''.join([x, 'aay']) for x in keywords.keys()])
    return t
print(cinfo(x=88, y=22, z=44))
