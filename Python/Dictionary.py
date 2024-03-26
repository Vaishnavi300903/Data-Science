# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 02:54:37 2024

@author: Dell
"""

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

#Dictonary comprehension

dict={x:x*x for x in range(3)}
print(dict)
























