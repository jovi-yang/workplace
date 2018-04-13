# coding=utf-8
# 习题1
a = [11, 22, 24, 29, 30, 32]
a.append(28)
a[0] = 6
i = a.index(29)
a.insert(i + 1, 57)
del a[a.index(32)]
a.sort()
print('习题1列表输出：{0}\n'.format(a))

# 习题2
b = [1, 2, 3, 4, 5]
c = [6, 7, 8]
d = b.extend(c)
print('习题2.1列表输出：{0}\n'.format(b))
b = [1, 2, 3, 4, 5]
print('习题2.2列表输出：{0}\n'.format(b + c))
bool1 = 2 in b
print('习题2.3列表输出：{0}\n'.format(bool1))

# 习题3
b = [23, 45, 22, 44, 25, 66, 78]
c = [x for x in b if x % 2 == 1]
print('习题3.1列表输出：{0}\n'.format(c))
d = ['the content ' + str(x) for x in b[:2]]
print('习题3.2列表输出：{0}\n'.format(d))
e = [x + 2 for x in b]
print('习题3.1列表输出：{0}\n'.format(e))

# 习题4
a = [x * 11 for x in range(1, 4)]
print('习题4输出：{0}\n'.format(a))

# 习题5
a = (1, 4, 5, 6, 7)
bo = 4 in a
print('习题5.1输出：{0}\n'.format(bo))
l = list(a)
l[l.index(5)] = 8
b = tuple(l)
print('习题5.2输出：{0}\n'.format(b))

# 习题6
setinfo = set('acbdfem')
finfo = set('sabcdef')
setinfo.add('adc')
print('习题6.1输出：{0}\n'.format(setinfo))
setinfo.remove('m')
print('习题6.2输出：{0}\n'.format(setinfo))
print('习题6.3交集输出：{0}\n'.format(setinfo & finfo))
print('习题6.3并集输出：{0}\n'.format(setinfo | finfo))

# 习题7
liming = {'name': '李明', 'age': 25, 'score': {
    'chinese': 80, 'math': 75, 'english': 85}}
zhangqiang = {'name': '张强', 'age': 23, 'score': {
    'chinese': 75, 'math': 82, 'english': 78}}
print('习题7.2输出：')
liming_score = liming.get('score')
liming_score['python'] = 60
liming['score'] = liming_score
print('李明信息输出：{0}'.format(liming))
zhangqiang_score = zhangqiang.get('score')
zhangqiang_score['python'] = 80
zhangqiang['score'] = zhangqiang_score
print('张强信息输出：{0}\n'.format(zhangqiang))

print('习题7.3输出：')
zhangqiang_score = zhangqiang.get('score')
zhangqiang_score['math'] = 89
zhangqiang['score'] = zhangqiang_score
print('张强信息输出：{0}\n'.format(zhangqiang))

print('习题7.4输出：')
del liming['age']
print('李明信息输出：{0}'.format(liming))

print('习题7.5输出：')
zhangqiang_score = zhangqiang.get('score')
paixu = sorted(zhangqiang_score.items(), key=lambda x: x[1])
zhangqiang['score'] = dict(paixu)
print('张强信息输出：{0}\n'.format(zhangqiang))

print('习题7.6输出：')
if 'city' in zhangqiang:
    del zhangqiang['city']
else:
    print('bejing')
