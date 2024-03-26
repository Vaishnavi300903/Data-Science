# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 03:19:32 2024

@author: Dell
"""

#Tuple
tup = ("cherry", "cherry", "banana")
print(tup)
print(tup[2])

#once tuple is created, you cannot change its value
x = ("apple","banana","cherry")
x[1] = 'kiwi'
#'tuple' object does not support item assignment

#first convert into list
y = list(x)
y[1] = "kiwi"
#convert list into tuple
x = tuple(y)
print(x)

x = ("apple",2,"cherry")
print(x)

x = ("apple","banana","cherry")
print(x[1])

#to join two or more tuples you can use the '+' operator
tup1 = ('a',"b",'c')
tup2 = (1,2,3)
tup3 = tup1 + tup2
print(tup3)




