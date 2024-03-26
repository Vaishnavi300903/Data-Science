# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 04:08:27 2024

@author: Dell
"""

#Password generator

#password
users=["Admin","Employee","Manager","Worker","Staff"]
for i in users:
    if i=="Admin":
        print("Welcome Admin.")
    elif i=="Employee":
        print("Welcome Employee.")
    elif i=="Manager":
        print("Welcome Manager.")    
    elif i=="Worker":
        print("Welcome Worker.")
    elif i=="Staff":
        print("Welcome Staff.")    
    else:
        print("Welcome")

i=str(input("Enter Designation:"))
if i=="Admin":
    print("Welcome Admin.")
elif i=="Employee":
    print("Welcome Employee.")
elif i=="Manager":
    print("Welcome Manager.")    
elif i=="Worker":
    print("Welcome Worker.")
elif i=="Staff":
    print("Welcome Staff.")    
else:
    print("Welcome")

"""Password generator"""
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'

import string
adjectives=["Sleepy","Slow","Smelly","wet","fat","red"," yellow",
            " green","blue","purple", "proud"," brave","fluffy"]

nouns=["apple","bat","cat","dinosour","goat","toaster","Panda",
       "penguin","tasmaniandevil","girrafe","rabbit","monkey"]

import random
adjective=random.choice(adjectives)
noun=random.choice(nouns)
number=random.randrange(0,100)
char=random.choice(string.punctuation)
password=adjective+noun+str(number)+char
print("Your new password is : %s"%password)

for pas in hide(lengths(password)):
    print(pas,end="")

while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    char=random.choice(string.punctuation)
    password=adjective+noun.upper()+str(number)+char
    print("Your new password is : %s"%password)
    response=str(input("Do you want another Password?(If Yes press Y)"))
    if  response!="Y":
          break

