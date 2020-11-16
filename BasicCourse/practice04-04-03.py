# coding:utf-8

columns = 5
rows = 5
symbol = "★"

for c in range(columns):
	for r in range(rows-c):
		print(symbol, end="")		
	print()
	