# coding:utf-8


print("------1-------")

for a in range(1, 10+1):
    print(a)
    if (a % 2 == 0) and not (a % 3 == 0):
        print("〇")
    if (a % 3 == 0) and not (a % 2 == 0):
        print("×")
    if (a % 2 == 0) and (a % 3 == 0): 
        print("△")
    

print("------2-------")

 
for a in range(1, 10+1):
    print(a)
    if (a % 2 == 0) and (a % 3 == 0): 
        print("△")
    else:     
    	if a % 2 == 0:
        	print("〇")
    	if a % 3 == 0:
        	print("×")


print("------3-------")

for a in range(1, 10+1):
    print(a, end="\t")
    if (a % 2 == 0) and (a % 3 == 0): 
        print("△")
    elif a % 2 == 0:
    	print("〇")
    elif a % 3 == 0:
    	print("×")
    else:
    	print("-")	