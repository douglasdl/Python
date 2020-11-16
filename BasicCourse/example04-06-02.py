# coding:utf-8

a = "abc"

def test():
	global a
	a = "def"
	print(a)
	return

test()
print(a)
