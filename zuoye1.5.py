#coding=utf-8
a = [1,2,3,4,5,333,11,44]
print("第一题：{0}\n".format(a[3:6]))

a = [1,2,3]
b = [4,5,6]
print("第二题第一种输出{0}\n".format(a+b))
a.extend(b)
print("第二题第二种输出{0}\n".format(a))

"""
c = ','.join([str(a),str(b)])
print(c)
"""

a = [1,2,99,33,44,55,22]
b = [11,33,54]
a.append(tuple(b))
print("第三题输出第一种结果：{0}\n".format(a))
a = [1,2,99,33,44,55,22]
a.insert(4,101)
print("第三题输出第二种结果：{0}\n".format(a))

a = [x for x in range(100) if x % 2 ==0 and x >= 20]
print("100内的大于20的偶数：\n{0}".format(a))
