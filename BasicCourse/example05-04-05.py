# coding:utf-8
import re

isOK = False
while isOK == False:
	b = input("数を入れてね＞")
	if not re.match(r"^\d\d\d\d$", b):
		print("4桁の文字を入力してください")
	else:	
		isOK = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])