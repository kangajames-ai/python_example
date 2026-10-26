

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking-Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Create a variable outside of a function, and use it inside the function
a = "awesome"

def myfunc():
  print("Python is " + a)

myfunc()

#Create a variable inside a function, with the same name as the global variable
a = "awesome"

def jay():
  a = "fantastic"
  print("Python is " + a)

jay()

print("Python is " + a)

i = 1    # int
j = 2.8  # float
k = 1j   # complex

print(type(i))
print(type(j))
print(type(k))

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

import random
print(random.randrange(1, 10))

#String Length
a = "Hello, World!"
print(len(a))
