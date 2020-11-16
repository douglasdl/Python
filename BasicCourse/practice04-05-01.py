# coding:utf-8

nen = 1968

print("うるう年？")
print(str(nen) + "は", end="")
if nen % 400 == 0:
	print("うるう年", end="") 
elif (nen % 4 == 0) and not (nen % 100 == 0): 
	print("うるう年", end="")
else:
	print("平年", end="") 
print("です。")	