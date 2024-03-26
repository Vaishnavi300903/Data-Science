# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 03:22:41 2024

@author: Dell
"""

#Generator
"""
It is another way of creating iterators in a simple way where it 
uses the keyword yeild instead of returning it in a defined 
function. Generators are implemented using a function.
"""
gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

gen=(x for x in range(3))
next(gen)
next(gen)
next(gen)

#FUnction which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)


gen=range_even(6)
next(gen)
next(gen)
next(gen)

#Chaining generators
def lengths(itr):
    for ele in itr:
        yield len(ele) #omly appllied for generator
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
"""
ele* appears to be a placeholder for an element from an iterable.
The asterisk * is likely just a character used to represent a 
placeholder or wildcard. For instance if you are iterating over 
a list of elements ele* could symoblize any element in that list.
It is a generic representation that dosen't correspond to any 
specific syntax in python or iter tools
"""

passwords=["not-good","give_me_pass",'00100=100']
for password in hide(lengths(passwords)):
    print(password)









































