# coding=utf-8
a = (1, 2, 3)
b = list(a)
b[0] = 5
c = tuple(b)
print("第一种输出：{0}\n".format(c))

b = list(a)
b.insert(1, 5)
del b[0]
c = tuple(b)
print("第二种输出：{0}\n".format(c))

bool1 = 2 in a
print(bool1)

a = set(['a', 'b', 'c'])
a.add('jay')
b = set(['b', 'e', 'f', 'g'])
c = a | b
print(c)
