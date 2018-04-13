#coding=utf-8
# 1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
def func1(*argu):
	for i in argu:
		if isinstance(i,int):
			pass
		else:
			return "请确认输入是否全是整数！"
	a = sorted(argu)
	return 'Max is {0}; Min is {1}.'.format(a[-1],a[0])

t = func1(1,2,3,4,5,'a')
print(t)
t = func1(1,2,3,4,5)
print(t)
# 2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
def func2(*arguments):
	t = filter(lambda i:isinstance(i,str), arguments)
	a = sorted(t,key=lambda i:len(i))
	return 'Max loggest string is {0}, Min shotest string is {1}'.format(a[-1],a[0])

f = func2('12','asdfae','sdd')
print(f)
# 3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
# 例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
import os
def get_doc(m):
	c = 'python -m pydoc %s' % m
	f = os.popen(c).read()
	return '{0}的帮助文档：\n{1}'.format(m,f)

f = get_doc('urllib')
print(f)

# 4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
import pathlib
def get_text(f):
	path = pathlib.Path(f)
	if path.is_file():
		with open(f,'r') as f2:
			text = f2.read()
		return text
	else:
		return "你输入的文件不存在，请重新输入！"

f = get_text('D:\\Programs\\Python36\\workplace\\test23.txt')
print(f)
# 5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
import glob
def get_dir(folder):
	path = pathlib.Path(folder)
	if path.exists():
		return glob.glob(folder+'*.*')
	else:
		return '你输入的文件路径不存在，请重新输入！'

f = get_dir('D:\\Programs\\Python36\\workplace\\')
print(f)