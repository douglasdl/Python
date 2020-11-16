# coding:utf-8

def calcArea(radius, pi = 3.1415):
	area = pi * radius**2
	return area

r = 10
area = calcArea(r)	
print("半径" + str(r) + "の円の面積は" + str(area) + "です。")