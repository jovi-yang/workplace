#coding=utf-8
# 1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
def get_num(num):
	l = []
	for i in num:
		if not isinstance(i, int):
			return '你所输入的参数列表不是全INT整型！'
		elif i % 2 == 0:
			l.append(i)
	return l

q1 = get_num([1,2,3,4,5])
print(q1)
q2 = get_num([1,2,3,4,'a',5])
print(q2)

# 2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
import requests
def get_page(url):
	r = requests.api.get(url)
	# for i in r.text:
	# 	return i
	return r.text

# q2 = get_page('http://www.163.com')
# print(q2)

# 3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def func(*argu):
	for i in argu:
		if not isinstance(i, list):
			return '你所输入的参数列表不是列表！'
		else:
			for x in i:
				if not isinstance(x, int):
					return '列表参数中不是全整数！'
				else:
					pass
	l = list(map(lambda i:max(i), argu))
	l.sort()
	return l[-1]


q3 = func([1,2,9],[1,3,4],[6],['j'])
print(q3)


# 4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。
import pathlib
import glob
def get_dir(f):
	path = pathlib.Path(f)
	if path.exists():
		p = glob.iglob(f+'*')
		l = list(filter(lambda i:pathlib.Path(i).is_dir(), p))
		return l
	else:
		return 'Not dir'

f = get_dir('D:\\Programs\\Python36\\')
print(f)
