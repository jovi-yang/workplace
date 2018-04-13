# coding=utf-8
a = (1, 2, 3)
b = list(a)
b[2] = 4
print("第一题输出：{0}\n".format(tuple(b)))

a = ["{0} love python".format(x) for x in range(1, 11)]
print("第二题1小题输出：\n{0}\n".format(a))

b = [(x, y) for x in [0, 2] for y in [0, 2]]
print("第二题2小题输出：\n{0}\n".format(b))
