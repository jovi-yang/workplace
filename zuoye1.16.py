# coding=utf-8
"""
题目1：
假如a = 5  b = 3
做下面的题目：
1 如果a > 1 并且 a < 10 输出 'a=5'
2 如果a等于5并且b=3输出结果'a=5,b=3'
"""
a = 5
b = 3
if a > 1 and a < 10:
    print('a=5')
elif a == 5 and b == 3:
    print("a=5,b=3")
else:
    pass


"""
题目2：
a = 1,b = 2
用两种方法判断如果b大于a则输出 'b>a'
"""
a, b = 1, 2
#b = 2
if b > a:
    print("b>a")
else:
    pass

print("B>A") if b > a else print("b<=a")

"""
题目3：
a = 1,b = 2
用3元表达式的两种方法输出结果：1
"""
a, b = 1, 2
print([a, b][False])
