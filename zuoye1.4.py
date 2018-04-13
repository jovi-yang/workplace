#coding=utf-8
"""
s = "i,am,lilei"
b = s[2:4]
print(b)

c = s.split(',',2,)[1]
print(c)

"""
a = open('test.txt','r')
b = a.read(100)
print(b)
a.close()

c = len(b)
print("长度是：",c)

d = b.replace('\n','')
print("去除换行符后的字符串：",d)

"""
bb = open('test.txt','r')
for line in bb.readlines():
    line = line.strip('\n')
    print(line)

a.close()
"""
e = d.replace('2012','2013')
print(e)

f = len(d)//2-5//2
print("\n最中间的长度为5的子串为：%s" % e[f:f+5])

print("\n最后2个字符串",e[len(e)-2:len(e)])

g = e.find('2')
print(e[g:g+11])

import sys
import string
f = open('string.txt','w')
sys.stdout = f
help(string)
f.close()
