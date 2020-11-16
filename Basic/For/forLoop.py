# coding:utf-8

# Print each element from a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Print each character from a string
for x in "banana":
  print(x)

# Print each element from a list until find a scpecific element
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Print each element from a list until find a scpecific element (print previous element)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Print each element from a list and skip a scpecific element
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# Range (start = 0, end, step = 1)
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)  

for x in range(2, 30, 3):
  print(x)

# Medir varias strings
palavras = ["gato", "janela", "programador"]
for p in palavras:
    print(p, len(p))

# Percorra a array para copia-la e adicionar um item no comeco
for p in palavras[:]:
    if len(p) > 6:
        palavras.insert(0, p)
print(palavras)


# For-Else
for x in range(6):
  print(x)
else:
  print("Finally finished!")	


# Nested Loops  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# The pass Statement
for x in [0, 1, 2]:
  pass
