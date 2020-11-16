# coding:utf-8

weight = 65.7 # Kg
height = 1.70 # m
bmi = weight / height / height
print(bmi)

if bmi > 30:
	print("!!") 
elif bmi > 25: 
	print("!")
elif bmi > 19.5: 
	print("〇")	
else:
	print("△") 