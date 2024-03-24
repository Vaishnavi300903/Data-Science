# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 02:53:20 2024

@author: Dell
"""

print("Hello World")

######################################

""".py is default extension"""

#Variables
'''
Types of Numbers 
There are three types used to represent
numbers in Python;
these are integers (or integral) types,
floating point numbers and complex numbers.
'''
x = 1
print(x)
print(type(x))
x = 100000000000000000000000000000000000000000000000000000
print(x)
print(type(x))


age = input('Please enter your age:')
print(type(age))
print(age)

age1 = input('Please enter your age:')
print(type(age1))
print(age1)

age2 = input('Please enter your age:')
print(type(age2))
print(age2)

age = age1+age2
print(age)

'''Type casting, string into int'''

age1 = int(input('Please enter your age:'))
print(type(age1))
print(age1)

age2 = int(input('Please enter your age:'))
print(type(age2))
print(age2)

age = age1+age2
print(age)

######################################

'''
Floating point numbers
Real numbers or floating point numbers, are represented in
python using the IEEE 75 double-precision binary floating 
point numbers
'''
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

######################################

'''
Converting to floats
As with integers it is possible to convert other type such
an integer or a string into a float
'''
int_val = 100
string_val = '1.5'
float_val = float(int_val)
print("int value as a float:", float_val)
print(type(float_val))

float_val = float(string_val)
print("string value as a float:", float_val)
print(type(float_val))

######################################

#Complex numbers
c1 = 1
c2 = 3+2j
print('c1:',c1,',c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.real)
print(c2.imag)

######################################

#Boolean values
#Python supports another type called boolean;
#a boolean type can only be one of true or false
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))

######################################

#You can also convert strings into booleans as long a
#True or False (nothing else).
status = bool(input('OK it is confirmed?: '))
print(status)
print(type(status))

######################################

#Arithmetic Operators
'''

'''
home = 10
away = 15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

######################################

print(100/20)
print(type(100/20))

'''to ignore the fractional part then
there is an allternative version of the 
divide operator //.'''

print(100//20)
print(type(100//20))

'''interested in reminder'''

print('Modulus division 100 %m3:',100%3)
print('modulus division 3%2:',3%2)

'''to calculate power we are using **'''
a = 5
b = 3
print(a**3)

######################################

#Assignment operator
x = 0
x += 1
print(x)

######################################

#None value 
#python has a special type,
#the NoneType, with a single value, None.
winner = None
print(winner is None)

print(winner is not None)

winner = None
print('winner:', winner)
print('winner is None:',winner is None)
print('winner is not None:',winner is not None)
print(type(winner))

######################################

#flow of control using If statement
#Comparison Operators

num = int(input("Enter a number : "))
if num > 0:
    print(num)
    
#Else in an If statement
num = int(input("Enter yet another number:"))
if num < 0:
    print("its negative")
else:
    print("its not negative")

#The use of elif
savings = float(input("enter your savings"))
if savings == 0:
    print("Sorry no savings")
elif savings < 500:
    print('Well done')
elif savings < 1000:
    print('Thats a tidy sum')
elif savings < 10000:
    print('Welcome sir')
else:
    print('Thank You')
    
######################################

#Iteration / Looping
#while loop
count = 1
print('Starting')
while count <= 10:
    print(count)
    count+=1
    
######################################

#for loop
#loop over a set of values in range
print('Print out values in a range')
for i in range(2,10):
    print(i)
    print('Done')
###################################################    
    
    
###################################################
  
print("Only print code if all iterations completed")
num = int(input('Enter a number to check for:'))
for i in range(0,16):
    if i == num:
        break
    print(i)
print('Done')

######################################

#Now use an 'anonymous' loop variable
for _ in range (0,10):
    #print('.')
    print('.',end='')
    print()
    
######################################

#Odd Numbers
start , end = 4, 19
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")
        
######################################

#Even Numbers
start, end = 4,19
for num in range(start, end + 1):
    if num % 2 == 0:
        print(num,end = " ")
        
###################################################
#Break and Continue
fruits=["Apple","Banana","Cherry"]
for i in fruits:
    print(i)


#Break 
fruits=["Apple","Banana","Cherry"]
for i in fruits:
    print(i)
    if(i=="Banana"):
        break

fruits=["Apple","Banana","Cherry"]
for i in fruits:
    if(i=="Banana"):
        break
    print(i)

#continue:
fruits=["Apple","Banana","Cherry"]
for i in fruits:
    if(i=="Banana"):
        continue
    print(i)

###################################################


"""
range(): function

adding parameter:
    
"""
for x in range(2,6):
    print(x)
###################################################
"""
Nested loop:
    loop inside loop
"""
colors=["Green","Yellow","Red"]
fruits=["Guava","Banana","Apple"]
for x in colors:
    for y in fruits:
        print(x,y)

###################################################
#Function without argument
def my_fun():
    print("Hello world from my function")
    
my_fun()    

###################################################
#Function with argument
def my_fun(name):
    print("Hello"+name)
    
my_fun("Ram") 
###################################################
#Positional arguments: two or more than two arguments
def my_fun(name1,name2):
    print(name1+" "+name2)
    
my_fun("Hello","World") 

my_fun("World","Hello") 

###################################################
"""
Arbitary arguments: *args
If we don't know how many arguments that should be
passed into the function then add * before parameter name
"""
def my_fun(*greet):
    print(greet[0]+" "+greet[2])
    
my_fun("Hello","World","India") 

###################################################
"""
kwargs
use the name kwargs with **
it is used to pass key value 
"""

def my_fun(**kwargs):
    for key,value in kwargs.items():
        print("%s = %s"%(key,value))


my_fun(first="Hello",mid="World",last="India") 

###################################################
"""
Default function:
    shows default parameter if we call the function without argument
"""
def my_fun(country="Norway"):
   print("I am from " + country)
   
my_fun("India")
my_fun()
my_fun("Brazil")   

###################################################
#Passing a list as an argument

fruits=["Apple","Banana","Cherry"]
def my_fun(fruits):
    for x in fruits:
        print(x)

my_fun(fruits)


###################################################
#return values
def my_fun(x):
    return x*5

my_fun(5)
###################################################
#Passing function
def my_fun():
    pass
#having an empty function defination

###################################################
"""
Factorial:
"""
def factorial(x):
    if(x==1):
        return 1
    else:
        return(x*factorial(x-1))

factorial(3)
factorial(6)
###################################################
"""
Lamda function is a small function 
It can take any no. of arguments
but can only have one expression
"""
def add(a):
    sum=a+10
    return sum

add(20)

add=lambda a:a+10
print(add(10))

add=lambda a,b:a+b
print(add(5,6))

#Finding odd numbers from the list
lst=[34,12,64,75,13,63]
odd_list=list(filter(lambda x:(x%2!=0),lst))
print(odd_list)

#filter() methoid accepts 2 arguments a functon and a iterable

#Find even numbers
lst=[34,12,64,75,13,63]
even_list=list(filter(lambda x:(x%2==0),lst))
print(even_list)

lst=[34,12,64,75,13,63]
sqr_list=list(map(lambda x:(x**2),lst))
print(sqr_list)










