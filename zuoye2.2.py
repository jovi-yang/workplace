#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-13 16:19:02
# @Author  : jovi-yang (jovi_yang@foxmail.com)
# @Link    : https://github.com/jovi-yang/workplace
# @Version : $Id$

import os
# 1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。

def get_num(num):
	l = []
	for i in num:
		if isinstance(i,int)==False:
			return '你所输入的参数列表有错误！'
		elif i % 2 == 0:
			l.append(i)
	return l


q1= get_num([1,2,3,4,5])
print(q1)
q1= get_num([1,2,3,4,5,'a'])
print(q1)






# 2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。

# 3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。

# 4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。