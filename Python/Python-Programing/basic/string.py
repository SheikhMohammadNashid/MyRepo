#Data Types in python

#1.string data type
'''A string is simply a series of character.Anything inside a quote in python is considered a string'''

"This is a string"
                         #both can used to make a string
'This is also a string'


#Methods (A method is an action that Python can performon a piece of data) on string

#1.Changing Case in a string with Methods

name = "sheikh nashid"

print(name.title())

#Output: Sheikh Nashid

print(name.upper())

#Output: SHEIKH NASHID

print(name.lower())

#Output: sheikh nashid

#2.Combining or Concatinating Strings

'''Concatenating in Python means joining two or more strings (or sequences) together using the `+` operator.'''

first_name = "Sheikh"

last_name = "Nashid"

full_name = first_name + " " + last_name

print(full_name)

#output: Sheikh Nashid

#3.Adding whitespacing to string with Tabs or Newlines

print("Python")

#output:Python

print("\tPython")

#output: Python

print("Names:\nnashid\nfahad\nrayaan\nayaan")

'''output:Names:
               nashid
               fahad
               rayaan
               ayaan'''

#Stripping Whitespaces

language = "python "

language.rstrip()

print(language)

#output:"python" 

'''Same can done on lefte side using lstrip()'''




