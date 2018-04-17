#coding=utf-8
class students():
	"""docstring for students"""
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_course(self):
		self.score.sort()
		return self.score[-1]

zm = students('zhangming',20,[69,88,100,90])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())

lq = students('liqiang',23,[82,60,99])
print(lq.get_name())
print(lq.get_age())
print(lq.get_course())

class dictclass():
	def __init__(self,kword):
		self.kword = kword

	def del_dict(self,var1_key):
#		self.var1_key = var1_key
		del self.kword[var1_key]

	def get_dict(self,var2_key):
		if var2_key in self.kword:
			return self.kword[var2_key]
		else:
			return 'key值参数不存在！'

	def get_key(self):
		return self.kword.keys()

	def update_dict(self,kword1):
		self.kword.update(kword1)
		return self.kword.values()

dict1 = dictclass({'a':1,'b':2})
dict1.del_dict('a')
print(dict1.get_key())
print(dict1.get_dict('b'))
print(dict1.get_dict('c'))
print(dict1.update_dict({'c':3,'d':4}))





