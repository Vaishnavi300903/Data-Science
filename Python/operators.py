# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:54:52 2024

@author: Dell
"""

x,y,z = 5,6,7
print(x)
print(y)
print(z)

x,y,z = 5
print(x)
print(y)
print(z)

######################################

#global variable
x = 'awesome'
def my_function():
    print("Python is ", x)
my_function()

###################################

#global and local variables
x = 'awesome'
def my_function():
    x = 'fantastic'
    print("Python is ",x)
my_function()
print("Python is ",x)

###################################

#getting data types
x = 5
print(type(x))

x = range(6)
print(type(x))

x = {'name':'ram', 'age':29}
print(type(x))

#assigning values
x = 1
y = 2.3
z = 2+5j
print(type(x))
print(type(y))
print(type(z))

###################################


#Operator precedense
"""
Rule for mathematical operations
PEMDAS Rule
P:Paranthesis
E:Exponential"""

print(3*3+3/3-3)

#####################################################

#identity oprator
a = 1
b = 1
print(a is b)
print(a is not b)

#####################################################


#####################################################
