#!/usr/bin/env python
# coding: utf-8

# # Chapter 2: Variables and and Simple Data Types
# * A variable name is an **identifier**. 
# * May consist of letters, digits and underscores (`_`) but may not begin with a digit. 
# * Python is _case sensitive_. 
# * Each value in Python has a type that indicates the kind of data the value represents. 

# ####  Statement creates `x` and uses the **assignment symbol (`=`)** to give `x` a value. 

# In[1]:


x = "Hello Python"
print(x)


# ### Print a message

# In[2]:


message = "Hello World"


# In[3]:


print(message)


# ### Try to print a Simple Message: Store a message in a variable, and then print that message.

# In[7]:


message_2 = "How are you doing today?"
print(message_2)


# In[6]:





# In[ ]:





# # Strings

# ## A string is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use `single` or `double quotes` around your strings
# ### "This is a string."
# ### 'This is also a string.'

# ###  Build in String methods
# Directory: dir('  ')

# In[ ]:





# In[1]:


dir(" ")


# In[8]:


# make uppercase
message.upper()


# In[9]:


# make lowercase
message.lower()


# In[10]:


# capitalize

message.capitalize()


# In[11]:


# title
message.title()


# In[12]:


# Concatination
name = "Peter"
print("Well hello "+name+", how is it going?")


# In[ ]:


# length


# In[17]:


len(message)


# ## Practice1:
# 1. Personal Message: Store a person’s name in a variable, and print a message
# to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”
# 2. Name Cases: Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase.

# In[ ]:


name = "Peter"
print("Well hello "+name+", how is it going?")


# In[19]:


name.lower()


# In[21]:


name.upper()


# In[22]:


name.title()


# ## Adding Whitespace to Strings with Tabs or Newlines or  quotation
# * A backslash (`\`) in a string is the **escape character**. 
# * The backslash and the character immediately following it form an **escape sequence**. 
# 
# #### 2.4.2 Other Escape Sequences
# | Escape sequence | Description
# | :------- | :------------
# | `\n` | Insert a newline character in a string. When the string is displayed, for each newline, move the screen cursor to the beginning of the next line. 
# | `\t` | Insert a horizontal tab. When the string is displayed, for each tab, move the screen cursor to the next tab stop. 
# | `\\` | Insert a backslash character in a string.
# | `\"` | Insert a double quote character in a string.
# | `\'` | Insert a single quote character in a string.

# In[31]:


print("Insert a newline character in a string. \nWhen the string is displayed, for each newline, \nmove the screen cursor to the beginning of the next line.")


# In[41]:


print("Insert a horizontal tab. \tWhen the string is displayed, for each tab, move the screen cursor to the next tab stop")


# In[88]:


print("His name is \'Eric\'")


# In[89]:


print("List of chapters: \n\t\tString \n\t\tList \n\t\tTuple \n\t\tControl Structure")


# In[56]:


myName = "\nJameson\t"
print(myName)


# In[ ]:





# # Useful Methods to Strip a String
# 

# * lstrip
# * rstrip
# * strip

# In[90]:


message = " Programming Language "


# In[91]:


message.strip()


# In[92]:


message.lstrip()


# In[93]:


message.rstrip()


# ## Practice2
# 1. Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

# # Number

# # Data Types
# * `float` (floating point) - used for real numbers.
# * `int` (integer) - used for integers.

# ## Arithmetic Operator
# | Python operation | Arithmetic operator | Python expression
# | :-------- | :-------- | :-------- 
# | Addition | `+`  | `f + 7` 
# | Subtraction | `–` | `p - c` 
# | Multiplication | `*` | `b * m` 
# | Exponentiation | `**` |  `x ** y` 
# | True division | `/` | `x / y` 
# | Floor division | `//` | `x // y` 
# | Remainder (modulo) | `%` | `r % s` 
# 
# `Floor division` is an operation in Python that divides two numbers and rounds the result down to the nearest integer.

# In[26]:


3 + 5.66


# In[23]:


3*4


# In[24]:


print("The exponent: ", 2**3) #2^3


# In[25]:


print("The exponent of 5 squared is ",5**2)


# In[27]:


print("True division",5/2)


# In[28]:


print("Floor division", 5//2)


# In[33]:


print("The modulo/remainder",3%2)


# In[35]:


print("The modulo/remainder",58%3)


# ## Avoiding Type Errors with the str() Function

# In[40]:


age= 21
name="Ella"
print("The age of " + name + " is " + str(age))


# In[43]:


print("The age of " + name + " is ", age)


# In[44]:


print("The addition is ",53+38)


# In[46]:


print("Multiplication is ", 91 * 2)


# In[48]:


print("Division is ", 91/2)


# In[50]:


print("Subtraction is ", 91-38)


# ## Practice3 
# 1. Write addition, subtraction, multiplication, and division
# operations that each result in the number 91. Be sure to enclose your operations
# in print statements to see the results. You should create four lines that look
# like this:
# print(53 + 38)
# Your output should simply be four lines with the number 91 appearing once
# on each line.
# 2. Favorite Number: Store your favorite number in a variable. Then, using
# that variable, create a message that reveals your favorite number. Print that
# message.

# In[ ]:


print("Multiplication is ", 91 * 1)


# In[ ]:


print("Division is ", 91/1)


# In[51]:


print("Subtraction is ", 91-0)


# In[52]:


print("Addition is ", 91+0)


# In[53]:


favNumber = 17
print("My favorite number is ", favNumber)


# ## Getting Input from the User
# * Built-in **`input` function** requests and obtains user input.

# In[57]:


flower_name = input("Enter your favorite flower\'s name: ")


# In[58]:


favorite_day = input("Enter your favorite day: ")


# In[59]:


type(flower_name)


# In[60]:


type(favorite_day)


# In[61]:


fav_number=input("Enter your favorite number: ")


# In[62]:


type(fav_number)


# In[63]:


fav_number=int(input("Enter your favorite number: "))


# In[64]:


type(fav_number)


# In[ ]:





# ## Getting an Integer/ Float from the User
# * If you need an integer, convert the string to an integer using the built-in **`int` / `float` function**. 

# In[ ]:


fav_number=int(input("Enter your favorite number: "))


# In[66]:


type(fav_number)


# In[67]:


number = float(input("Enter a real number/ floating point number: "))


# In[68]:


type(number)


# In[69]:


print(type(number))


# ## Checking the data type using `type` function

# In[71]:


number = 23
name = "Jameson"
print(type(number))
print(type(name))


# In[ ]:





# ## Errors in Python
# When an error occurs in your program, the Python interpreter does its
# best to help you figure out where the problem is. The interpreter provides
# a traceback when a program cannot run successfully. A traceback is a record
# of where the interpreter ran into trouble when trying to execute your code.
# Errors can be classified into three major groups:
# - Syntax errors
# - Runtime errors
# - Logical errors

# ### Syntax error.
# - Python will find these kinds of errors when it tries to parse your program, and exit with an error message without running anything. 
# - Syntax errors are mistakes in the use of the Python language, and are analogous to spelling or grammar mistakes in a language like English: for example, the sentence Would you some tea? does not make sense – it is missing a verb.
# 

# ### Example:
# - leaving out a keyword
# - putting a keyword in the wrong place
# - leaving out a symbol, such as a colon, comma or brackets
# - misspelling a keyword
# - incorrect indentation
# - empty block

# In[72]:


print("This is an error message)


# In[73]:


print("This is an error message")


# In[76]:


len("Hello")=5


# In[77]:


1 = "python"


# ## Runtime error
# - A program with a runtime error is one that passed the interpreter’s syntax checks, and started to execute. 
# - However, during the execution of one of the statements in the program, an error occurred that caused the interpreter to stop executing the program and display an error message. 
# - Runtime errors are also called `exceptions` because they usually indicate that something exceptional (and bad) has happened.

# ### Examples: 
# - division by zero.
# - performing an operation on incompatible types.
# - using an identifier which has not been defined.
# - accessing a list element, dictionary value or object attribute which doesn't exist.
# - trying to access a file which doesn't exist.

# In[78]:


15/0


# In[ ]:


#Fix the errors
amount = input("Enter the total amount before tax: ")
tax=0.06
print("The total is: " amount*tax + Amount)


# In[84]:


amount=int(input("Enter the total amount before tax:"))
tax= 0.06
print("The total is: ",amount*tax +amount)


# ### Logical error
# - Logical errors are the most difficult to fix. They occur when the program runs without crashing, but produces an incorrect result. 
# - The error is caused by a mistake in the program’s logic. 
# - You won’t get an error message, because no syntax or runtime error has occurred. 
# - You will have to find the problem on your own by reviewing all the relevant parts of your code 

# In[86]:


number1=int(input("Enter an integer number: "))
number2=float(input("Enter a floating point number: "))
print("The product of number1 and number2 is :", number1+number2)


# In[87]:


print("The product of number1 and number2 is :", number1*number2)


# In[ ]:




