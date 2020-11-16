# coding: utf-8


# Fibonacci
n2 = 0
sum = 0
for n1 in range(1, 10 + 1):
    sum = n1 + n2
    print(str(n1) + " + " + str(n2) + " = " + str(sum))
    n2 = sum



# Vertical
print("")
for number in range(1, 9 + 1):
    print("九九の" + str(number) + "段")
    for n in range(1, 9 + 1):
        print(str(number) + " × " + str(n) + " = " + str(number * n))
    print("")


# Horizontal
for n2 in range(1, 9 + 1):
    for n in range(1, 9 + 1):
        print(str(n) + " × " + str(n2) + " = " + str(n * n2), end="\t")
    print()
