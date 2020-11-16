# coding:utf-8

def showMark(symbol, number):
	for n in range(number):
		print(symbol, end="")
	print()	

def showMark2(symbol, number):
	print(symbol * number)

def showMark3(columns, rows, symbol):
	for c in range(columns):
		for r in range(rows-c):
			print(symbol, end="")		
		print()

def showMark4(columns, rows, symbol):
	for c in range(columns):
		for r in range(rows):
			print(symbol, end="")		
		print()



showMark("★", 5)
print()
showMark2("〇", 5)
print()
showMark3(5, 5, "△")	
print()
showMark4(5, 5, "◇")
print()