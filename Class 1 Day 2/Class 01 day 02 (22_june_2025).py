print("hello world")
print("what is programming?")
print("In simple terms programming is giving instructions to a computer so it can do what you want ")
print()
print("what ia python language")
print("python is a programming language a simple way to talk to a computer it is made by Guido Van Rossum in 1991 ")
print("example:::")
x=1
print(x)
y=2
print(y)
z=x+y
print(z)
print()
print("what is modules in python")
print("A module in python is like a toolbox that contains readymade tools(code) that you can use in your program." \
"instead of write everything from scratch in your program you can just import a module and use its features__like functions variables or clases")
print("Why use modules?")
print("to save time , to rescue code others have already return")
print("exmaple:")
print("Python has a module called math. If you want to find a square root:")
import math
print(math.sqrt(16))
print()
# Two types of modules
'''Built-in modules → Already come with Python

Example: math, random, datetime

Custom modules → You can create your own .py files and use them as modules

Example: A file my_tools.py with your own functions

'''
# What is a variable in Python ):
'''A variable is like a container or box that holds some data (like a number, word, or list), so you can use it later in your program.

You give it a name, and Python remembers the value.'''

# ✅ Example:
'''
name = "Owais"
age = 18
name is a variable that holds the text "Owais"

age is a variable that holds the number 18'''

# You can now use them like this:

'''print(name)
print(age)'''

# Output:

'''Owais
18'''

a = 1   # variables to store an integer 
name = "owais" # variable to store a word
b = 2.5  # variable to store a floating point

# DATA TYPES IN PYTHON
'''Primeraly these are the following datatypes in python:
integer
floating point numbers
strings
booleans
none
'''

a = 12  # a is an integer 
b = 5.22  # b is a floating point
c = True  # c is a bolean datatype
d = "owais" # d ia a string
e = None # e is a none 

'''there is question why we use none when we need that tha variable must be 
empty so at that place we use None data type'''

# RULES FOR DEFINING A VARIABLE NAME
'''1 A variable name can contain alphabets,digits and underscore
   2 A variable name can only start with alphabets and underscore
   3 A variable name can't with a digit
   4 no while space allowed to be used inside a variable name 
   Examples of a variable name: owais,seven4,_seven stc'''

# OPERATORS IN PYTHON
'''1 Arithmetic operator: +,-,*,/
   2 Assignment operators: =,+=,-=
   3 comparison operators: ==,>=,<,!=
   4 logical operators: and,or,not
   '''
1 + 2 = 3
# +  = operator
# 1 and 2 = operands
# 3 = result

# TYPE() FUNCTION AND TYPE CASTING
'''TYPE FUNCTION IS USED TO FIND THE DATA TYPE OF THE GIVE VARIABLE IN PYTHON FOR eg'''
a =2
type(a)  # class <int>

b = '31'
type(b)  # class <str>

'''a number can be converted into a string and viseversa (if possible)'''

# INPUT() FUNCTION
'''this function allows the user to take input from the keyboard as a string'''
a = input("enter num")  # if a is 'harry' the users entered harry
'''it is important to note that the output of input is always a string(even is a number is entered)'''
# chage input function another data type 
a = int(input("enter a number")) # now the num we enter that int data tyoe change it into integer