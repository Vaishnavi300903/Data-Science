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

#####################################################
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

#####################################################

#Dictionary
dict = {"Brand" : "Lambo","model" : "Aventador","yr":2011}
print(dict)
print(len(dict))
print(type(dict))

dict = {
        "Brand" : ["Lambo","audi","bugatti"],
        "model" : ["Aventador","R8","chiron"],
        "yr":[2011,2023,2021]
        }
print(dict)

dict = {"Brand" : "Lambo","model" : "Aventador","yr":2011}
print(dict)
print(len(dict))
print(type(dict))
dict.get("model")
dict.keys()

###################################################
#How to add element into the dictionary
car={
     "Brand":"Ford",
     "Model":"Mustang",
     'year':1964
     }
x=car.keys()
print(x)
car["Color"]="White"
car
x=car.keys()
print(x)
#New key and values are inserted in the dictionary
###################################################
#How to remove element into the dictionary
"""
pop method used in dictionary needs key
pop method used in list needs index
"""
car={
     "Brand":"Ford",
     "Model":"Mustang",
     'year':1964
     }
car.pop("Model")
print(car)
###################################################

#Accessing keys in the dictionary
for x in car:
    print(x)

#Accessing values in the dictionary
for x in car:
    print(car[x])

#Accessing both keys and values
for key,value in car.items():
    print("%s = %s"%(key,value))
    
###################################################
#Copying  dictionary
car2=car.copy()
car2

#Another way to make a copy to use the dictionary is this dict

d={
     "Brand":"Ford",
     "Model":"Mustang",
     'year':1964
     }
dict1=dict(d)

#We can use dict function to create a new dictionary

###################################################
#Dictionary inside dictionary "nested dictionary"
family={
        "child1":{
            "Name":"Ram",
            "D.O.B":"21-05-2008"},
        "child2":{
            "Name":"Shyam",
            "D.O.B":"21-05-2008"}
        }

family
family["child1"]

###################################################
#Dictionary methods
#clear():Remove all the elements from the dictionary
car={
      "Brand":"Ford",
      "Model":"Mustang",
      'year':1964
      }
car.clear()
car
###################################################
#copy():Copy the dictionary into another dictionary
car2=car.copy()
car2

###################################################
#fromkey()
x={'key1','key2','key3'}
y=0
d=dict.fromkeys(x,y)
d

###################################################
#get():To get the value of dictionary
car={
      "Brand":"Ford",
      "Model":"Mustang",
      'year':1964
      }
car.get("Model")

###################################################
#items():Return the dictionaries key-value
car.items()

####################################################
#pop():Removes the specified key values
car.pop("Model")

###################################################
#values():display all the values of dictionary
car.values()

###################################################
#update():Insert an item into a dictionary
car.update({"Color":"White"})
car

####################################################
#We can also change the value  by using update

