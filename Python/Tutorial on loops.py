# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 02:58:26 2024

@author: Dell
"""

"""
Write python code using logical operator  so as to check height as well 
as age and the cost of ride
"""
def switch(ch):
   global bill
   switch_case = {
    1: 50, 
         
    2:20,
           
    3:30
       
     }
   price = switch_case.get(ch, 0)  
    
   bill += price
   print("Thankyou for paying your bill:",bill)  
   print("Enjoy your ride.")
  
   
  
print("Welcome to the roller coaster")
height=int(input("Enter your Height in centimeter:"))
if height>=120:
    print("Congragulations!!! You are eligible for roller coaster ride")
    age=int(input("Enter your age in years:"))
    bill=0
    
    if age<12:
        print("Ticket price: 10$")
        bill=10
        print("Please pay bill:",bill)
    elif age>=12 and age<20:
        print("Ticket price: 20$")
        bill=20
        print("Please pay bill:",bill)
    elif age>=20 and age<40:
        print("Ticket price: 30$")
        bill=30
        print("Please pay bill:",bill)
    elif age>=40 and age<60:
        print("Ticket price: 40$")
        bill=40
        print("Please pay bill:",bill)
    else:
        print("You are not eligible.")
        
    service=str(input("Do you want any other service?(If Yes press Y)"))
    if service=="Y" :
        print("Service name:\n1.Popcorn\n2.Cold-drink\n3.Photo")
        ch=int(input("Enter your choice code:"))
        switch(ch)
    else: 
        print("Thankyou for paying your bill:",bill)  
        print("Enjoy your ride.")
              
else:
    print("You are not eligible.")


"""
Calculation of BMI
"""


height=float(input("Please enter your height in meter:"))
weight=float(input("Please enter your weight in kg:"))
BMI=round((weight/(height*height)),2)   

if BMI<18.5:
    print(f"You are under weight and your BMI is:{BMI}")
elif BMI>=18.5 and BMI<25:
    print(f"You are normal weight and your BMI is:{BMI}")
elif BMI<25 and BMI<30:
    print(f"You are over weight and your BMI is:{BMI}")
elif BMI>=30 and BMI<35:
    print(f"You are obese and your BMI is:{BMI}")
else:
    print(f"You are clinically obese and your BMI is:{BMI}")

"""
Write a program to find out duplicate elements from the list
"""
lst1=[1,2,3,4,5,6,7,6,8,1,4]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #Compare the current number with next number
        for j in range(len(lst1)-1):
          if(lst1[i]==lst1[j]):
              return True
    return False
    
print(is_duplicate(lst1))    

lst1=[1,2,3,4,5,6,7,6,8,1,4]
lst1.sort()
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        #Compare the current number with next number
          if(lst1[i]==lst1[i-1]):
              return True
    return False

print(is_duplicate(lst1))       

"""
Leap year
"""
def is_leap_year(year):
    if ((year>0) and (year%4==0) and (year%100!=0) or (year%400==0)):
        return True
    return False


print(is_leap_year(2000))
print(is_leap_year(2999))
print(is_leap_year(2024))
print(is_leap_year(2004))
print(is_leap_year(1900))

"""
Mario pyramid
"""
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()    


for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()  

for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()  


#Minimum and maximum
lst=[34,12,64,75,13,63]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("The minimum value is", min)
    max=lst[0]
    for i in lst:
        if i>max:
           max=i
print("The minimum value is", max)

#Palindrome
def is_palindrome(input):
    
   string=input[::-1]
   if string ==input:
       return True
   return False


print(is_palindrome("12321"))


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



