# coding:utf-8
import random

isOK = False
while isOK == False:
	b = input("数を入れてね＞")
	if len(b) != 4:
		print("4桁の文字を入力してください")
	else:
		kazuOK = True
		for i in range(4):
			if (b[i] < "0") or (b[i] > "9"):
				print("数字ではありません")
				kazuOK = False
				break
		if kazuOK:	
			isOK = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])