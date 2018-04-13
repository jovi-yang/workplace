a = "this is a %s %s." % ("apple",19)
print(a)

b = "this is a {1} {0}." .format ("apple","my")
print(b)

b = "this is a {whose} {fruit}." .format (fruit="apple",whose="my")
print(b)


a = "this is %(whose)s %(fruit)s" % {'whose':'my','fruit':'apple'}
print(a)


a = 'pyer'
b = 'apple'
c = "my name is {0}, i love {1}." .format(a,b)
print(c)

d = "my name is %(name)s, i love %(fruit)s." % {'fruit':'apple', 'name':'pyer'}
print(d)
