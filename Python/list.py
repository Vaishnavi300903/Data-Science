# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 02:54:07 2024

@author: Dell
"""
#Python list
lst = ["cherry","banana","apple"]
print(lst)

#list items are indexed, starting with 0
print(lst[0])
print(lst[2])

#append() : Adds an element at the end of the list
lst = ["cherry","banana","apple"]
lst.append("Mango")
print(lst)

#clear() : all items are gets remove
lst = ["cherry","banana","apple"]
lst.clear()
print(lst)

lst = ["cherry","banana","apple"]
lst2 = lst.copy()
print(lst2)

#count the cherry 
lst = ["cherry","cherry","apple"]
lst.count("cherry")

#extend() : add the elements of one to another list
lst = [1,3,34]
lst1 = [4,5,6]
lst.extend(lst1)
print(lst)

lst = ["cherry","cherry","apple"]
lst.insert(1,"Mango")
print(lst)

#pop() : remove the element from perticular location
lst = ["cherry","cherry","apple"]
lst.pop(2)
print(lst)

#remove() : rremove the element by its item name
lst = ["cherry","cherry","apple"]
lst.remove("cherry")
print(lst)

#reverse() : reverse the list
lst = ["cherry","cherry","apple"]
lst.reverse()
print(lst)

#sort() : sort alphabetically
lst = ["cherry","cherry","apple"]
lst.sort()
print(lst)


lst=[]
for num in range (0,20):
    lst.append(num)
print(lst)    

#List Comprehension

lst=[num for num in range(0,20)]
print(lst)

names=['dada','mama','kaka']
lst=[name.capitalize() for name in names ]
print(lst)

#List comprehenssion with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(0,10) if is_even(num)]
print(lst)

#List comprehenssion with for loop
lst=[f"{x}{y}"for x in range(3) for y in range(3) ]
print(lst)

#ENumerate
#printing list with index

lst=['milk','eggs','bread']
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')

#Same code implemented using enumerate
lst=['milk','eggs','bread']
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")

#Use of zip function
name=['dada','mama','kaka']
info=[9870,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)

#Use of zip function with missmatch list
name=['dada','mama','kaka','baba']
info=[9870,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
#it will not display   excess item

#Zip longest
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9870,6032,9785]
for nm,inf in zip_longest(name,info):
    print(nm,inf)


#fill value instead none
from itertools import zip_longest
name=['dada','mama','kaka','baba']
info=[9870,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)

#Use of all() if all the values are true then it will produce 
#output
lst=[2,4,6,-8,9]
if all(lst):
    print("All values are true")
else:
    print("there are null values")
     
lst=[2,4,6,0,9]
if all(lst):
    print("All values are true")
else:
    print("there are null values")
     
#Use of any one non-zero va;ues
lst=[0,0,0,-8,0]
if any(lst):
    print("there are some zero value")
else:
    print("Useless")
     
#Use of any one non-zero va;ues
lst=[0,0,0,0,0]
if any(lst):
    print("there are some zero value")
else:
    print("All values are null")
     
#count()
from itertools import count
counter=count()
print(next(counter))

#Start from 1
from itertools import count
counter=count(start=1)
print(next(counter))

#cycle()
#Suppose you have to repeat tasks to be done 
import itertools
instructions=("Eat","Code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)

#repeat()
from itertools import repeat
for msg in repeat ("Keep patience",times=3):
    print(msg)

#combinations()
from itertools import combinations
players=['jhon','jani','janardan']
for i in combinations(players, 2):
    print(i)

from itertools import combinations
players=["A","B","C","D","E","F","G","H","I"]
for i in combinations(players, 5):
    print(i)

#Permutations()

from itertools import permutations
players=['jhon','jani','janardan']
for i in permutations(players, 2):
    print(i)

from itertools import permutations
players=["A","B","C","D"]
for i in permutations(players, 4):
    print(i)

#product()
from itertools import product
team_a=['Rohit','Pandya','Bumrah']
team_b=['Virat','Manish','Sami']
for pair in product (team_a,team_b):
    print(pair)

age=[27,17,21,19]
adults=filter(lambda age:age>18,age)
print(age for age in adults)
"""
In python , assignment statements (obj_a,obj_b) do not create real 
copies 
It only creates a new variable with the same referance
So when you want to make actual copies of mutable objects and 
want to modify th copy without affecting the orignl, you have 
to be careful
For real copies you can use the copy module
however for compund/nested objects and custom objects there is 
an important differance between shallow and deep copying

Shallow opies: only one level deep
creates new collection and populates its referacne to neated 
object
deep copies:full independent clone
creates new collection and then recurssively populates it with 
copies of nested  
    
"""
#Assignment operaton
#This will only create a new variable with same referance.\
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)













































