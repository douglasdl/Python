def myFunction():
	return 0

def myFunction2(parameter):
	return parameter * 2

# Use Parameters
def add (a, b):
	sum = a + b
	print(sum)
add(2,3)

# Use Return
def add (a, b):
	return a + b
x = add(2,3)
y = add(5,10)
total = add(x,y)
print(total)

# Default Parameter
def add (a, b = 5):
	return a + b
x = add(2,3)
print(x) # 5
y = add(7)
print(y) #112
total = add(x,y)
print(total)

# Keyword Arguments
def add (a, b):
	return a + b
x = add(a = 2, b =3)
print(x) # 5
y = add(b = 7, a=11)
print(y) #16
total = add(b=x,a=y)
print(total)

# Built-in function
a = min(2,3,-1,0)
c = pow(2,3)
d = len("string")
g = type(e)
print(a)
print(b)
print(c)
print(d)
print("$" + e)
print(f * 2)
print(g)

# Type Conversion
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = list("word")
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))


# Use docstring
def add (a, b):
	""" Add two numbers or two strings """
	return a + b


# Anonymous function
double = lambda x: x * 2
# Output: 10
print(double(5))

# Access global variable
c = 5
def add (a, b):
	c = a + b
	return c
# will get an exception
x = add(12, 23)
# use global
def add (a, b):
	global c
	c = a + b
	return c

# return more than one value
"""
def get_a_lot(x):
	y0 = x + 1
	y1 = x * 3
	y2 = y0 ** y3
	return (y0, y1, y2)
things = get_a_lot(5)

"""

# Variable-length argument
def add_everything(*args):
	return sum(args)
# Calculate the sum
print(add_everything(1,4,5, 75, 112))

#Pass by reference vs value
# Define `main()` function
def main():
  hello()
  print("This is a main function")
  
# Execute `main()` function 
if __name__ == '__main__':
    main()