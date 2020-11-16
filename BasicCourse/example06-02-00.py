# coding:utf-8
import random

a = [random.randint(0, 9),
random.randint(0, 9),
random.randint(0, 9),
random.randint(0, 9)]

# テストのための答え表示
#print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))

while True:
	# 4桁の数字かどうかを判定する
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
	# 4桁の数字であったとき
	# ビットを判定
	hit = 0
	for i in range(4):
		if a[i] == int(b[i]):
			hit = hit + 1

	# ブローを決定
	blow = 0
	for j in range(4):
		for i in range(4):
			if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
				blow += 1
				break

	# ビットとブロー数を表示
	print("ヒット " + str(hit))
	print("ブロー " + str(blow))

	# ヒットが４なら当たりで終了
	if hit == 4:
		print("当たり！")
		break