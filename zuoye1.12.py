#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-20 21:05:17
# @Author  : jovi yang (jovi_yang@yeah.net)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$
import copy
ainfo = {'ab': 'liming', 'ac': 20}
binfo = copy.deepcopy(ainfo)
ainfo['sex'] = 'man'
ainfo['age'] = 20
print("第一种输出: %s\n" % ainfo)

binfo.update({'sex': 'man', 'age': 20})
print("第一种输出: %s\n" % binfo)

ainfo = {'ab': 'liming', 'ac': 20}
a = ainfo.keys()
print(a)
print(ainfo.values())

print("\n返回‘ab’的值！")
print(ainfo['ab'])
print(ainfo.get('ab'))

print("\n删除键名‘ab’的值！")
del ainfo['ab']
print(ainfo)

ainfo = {'ab': 'liming', 'ac': 20}
ainfo.pop('ab')
print(ainfo)
