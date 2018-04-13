#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-26 21:28:18
# @Author  : jovi yang (jovi_yang@yeah.net)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : $Id$

'''
1. 已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
1.1 请将a字符串的大写改为小写，小写改为大写。
1.2 请将a字符串的数字取出，并输出成一个新的字符串。
1.3 请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':4,'b':2}
1.4 请去除a字符串多次出现的字母，仅留最先出现的一个。例 'abcabb'，经过去除后，输出 'abc'
1.5 请将a字符串反转并输出。例：'abc'的反转是'cba'
1.6 去除a字符串内的数字后，请将该字符串里的单词重新排序（a-z），并且重新输出一个排序后的字符 串。（保留大小写,a与A的顺序关系为：A在a前面。例：AaBb）
1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
1.9 输出a字符串出现频率最高的字母
'''
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = a.upper()
print('1.1大写字符：%s' % b)
c = a.lower()
print('1.1小写字符：%s' % c)

l = list(a)
for x in l:
    if x.isnumeric():
        l.remove(x)
    else:
        pass
New_a = ''.join(l)
print('1.2数字取出，并输出成一个新的字符串：%s' % New_a)

New_b = []
tb = list(New_a.upper())
for x in tb:
    n = tb.count(x)
    m = (x, n)
    New_b.append(m)
dict1 = dict(set(New_b))
print('1.3每个字母的出现次数，并输出成一个字典：%s' % dict1)

l4 = list(New_a)
l41 = []
for x in l4:
    if x not in l41:
        l41.append(x)
    else:
        pass
a5 = ''.join(l41)
print('1.4去除a字符串多次出现的字母，仅留最先出现的一个：%s' % a5)

n = len(a)
x = 0
a_test = []
while x != n:
    a_test.append(a[n - 1 - x])
    x += 1
else:
    pass
print('1.5将a字符串反转并输出：%s' % ''.join(a_test))

t6 = [(x.upper(), x) for x in New_a]
t6.sort()
l6 = []
for x in t6:
    if ord(x[0]) == ord(x[1]):
        l6.append(x[0])
    else:
        l6.append(x[1])
print('1.6重新输出一个排序后的字符：%s' % ''.join(l6))

# 1.7 请判断 'boy'里出现的每一个字母，是否都出现在a字符串里。如果出现，则输出True，否则，则输 出False.
str1 = 'boy'
set1 = set(str1)
set2 = set(a)
for x in set1:
    if x in set2:
        print(x + ': True')
    else:
        print(x + ': False')
print('*' * 50)

# 1.8 要求如1.7，此时的单词判断，由'boy'改为四个，分别是 'boy','girl','bird','dirty'，请判断如上这4个字符串里的每个字母，是否都出现在a字符串里。
set1 = set('boy')
set2 = set('girl')
set3 = set('bird')
set4 = set('dirty')
set_all = set1 | set2 | set3 | set4
for x in set_all:
    if x in set(a):
        print(x + ': True')
    else:
        print(x + ': False')

# 1.9 输出a字符串出现频率最高的字母
New_l = []
tl = list(a)
for x in tl:
    n = tl.count(x)
    m = (x, n)
    New_l.append(m)
d = dict(New_l)
l = max(d.items(), key=lambda x: x[1])
print('1.9输出a字符串出现频率最高的字母：{0}\n'.format(l[0]))

# 2.在python命令行里，输入import this 以后出现的文档，统计该文档中，"be" "is" "than" 的出现次数。
import os
cmd1 = "echo import this > D:\\Programs\\Python36\\workplace\\this.py"
if os.path.exists('this.py'):
    os.remove('this.py')
else:
    os.popen(cmd1)
a = 'be'
b = 'is'
c = 'than'
n_a, n_b, n_c = 0, 0, 0
f = open('this.txt', 'r')
f_str = f.readlines()


def count_str(s):
    n = 0
    for x in f_str:
        if s in x:
            n = s.count(s) + n
        else:
            pass
    return n


n_a = count_str(a)
n_b = count_str(b)
n_c = count_str(c)
print('2.0 "be" "is" "than" 的出现次数分别为：{0}; {1}; {2}'.format(n_a, n_b, n_c))

# 3.一文件的字节数为 102324123499123，请计算该文件按照kb与mb计算得到的大小。
bit = 102324123499123
kbit = bit >> 10
mbit = bit >> 20
print(kbit, mbit)

# 4.已知  a =  [1,2,3,6,8,9,10,14,17],请将该list转换为字符串，例如 '123689101417'.
a = [1, 2, 3, 6, 8, 9, 10, 14, 17]
aa = [str(x) for x in a]
b = ''.join(aa)
print(b)
