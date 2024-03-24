# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:02:10 2024

@author: Dell
"""

"""
String:
    
    Single line string: single quotation mark('')
                        double quotation mark("")
    Multiline string: single quotation mark('''  ''')
                      double quotation mark("""  """)                    
""" 

x = "Hello World."
print(x)
######################################################

# multiline strings
x1 = """This is python. It is very powerfull"""
print(x1)

######################################################

#String length: len() function

len(x)
len(x1)

######################################################

#Accessing characters from string
print(x[5])
print(x1[1])

######################################################

#To check if certain character is present in string or not

txt="The best things in life are free of cost"
print("free" in txt)

txt="The best things in life are free of cost"
print("free" not in txt)

#Using for loop
if "free" in txt:
    print("Free is present in txt")
else:
    print("False")    
######################################################
#String slicing

print(x[2:8])


#slice from the start
print(x[:3])

#Slicing to the end
print(x[5:])

#Negative indexing
print(x[-5:-2])

######################################################

#Modify strings
print(x.upper())

print(x.lower())

######################################################
#remove white spaces(only initial left)
x = "    This is python    "
x
print(x.strip())

x = "  This is python   "
print(x.lstrip())

x = "  This is python  "
print(x.rstrip())

######################################################

#Replace string
x = "Hello world"
print(x.replace("Hello","Gello"))

######################################################

x = "Hello world"
print(x.split(" "))

######################################################

x = "Hello World"
string1 = x[::-2]
print(string1)
print(x[::-1])

######################################################

#String Concatenation

x = "hello"
y = "world"
print(x+ " " +y)

######################################################

#string error 
x = 36
y = "my name is anthony"
print(x+y)
#unsupported operand type(s) for +: 'int' and 'str'

str1 = "hello"
str2 = 2
str3 = str1 + str2
#error : can only concatenate str (not "int") to str


print(f"my name is anthony and my age is {x}")

quantity = 3
item_no = 54
price = 67
print(f"I want {quantity} pieces and item number is {item_no} and its price is {price}")

my_order = "I want {} pieces and item number is {}, its price is {}"
print(my_order.format(quantity,item_no,price))

quantity = 3
item_no = 54
price = 67
my_order = "I want {0} pieces and item number is {1}, its price is {2}"
print(my_order.format(quantity,item_no,price))

######################################################

#The escape characters allows you to use double qoutes when you want
text = "This is fun and it has got big \"round rigo\""
#text = "This is fun and it has got big \"round rigo\""
print(text)

######################################################

#find method, Searches the string for a specified value
#getting its index
x = "This id python and it is very powerful"
print(x.find("and"))


