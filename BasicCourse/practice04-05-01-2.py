# coding:utf-8

nen = 1968
hantei = ""

if nen % 400 == 0:
	hantei = "うるう年"
elif (nen % 4 == 0) and not (nen % 100 == 0): 
	hantei = "うるう年"
else:
	hantei = "平年"
print(str(nen) + "年は" + hantei + "です。")	