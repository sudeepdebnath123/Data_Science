#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Types of Parametrs
    1. Positional Parameters
    2. Default Parameters
    3. Keyworded Arguments
    4. Variable length positional arguments - *args
    Variable length keyworded arguments - **kwargs


# In[1]:


a = 10


# In[4]:


# def my_fun(a, b, c):
#     print(a, b, c)
    
# my_fun(10, 20)


# In[27]:


# Default Parameter - 
#     1. Default parameter should always follow the positional parameter.

# d = {1:100, 2:200, 3:300}
# d.get(1)
# print(d.get(10))

# lst = [10,20,30,40]
# lst.index(10)



# Write a method in python to display the elements of list thrice if it is a number and display 
# the element terminated with ‘#’ if it is not a number.

# For example, if the content of list is as follows :
# ThisList=[‘41’,‘DROND’,‘GIRIRAJ’, ‘13’,‘ZARA’]
# The output should be
# 414141
# DROND#
# GIRIRAJ#
# 131313
# ZARA#

def my_fun(lst, num_of_times = 3, terminating_val = '#'):
    for i in lst:
            if i.isnumeric():
                print(i*num_of_times)
            else:
                print(i + terminating_val)

# my_fun(['41','DROND','GIRIRAJ', '13','ZARA'])
# my_fun(['41','DROND','GIRIRAJ', '13','ZARA'], '$')


# In[28]:


# Keyworded Arguments
# Keyworded argument should always follow the positional arguments.


def my_fun(lst, num_of_times = 3, terminating_val = '#'):
    for i in lst:
            if i.isnumeric():
                print(i*num_of_times)
            else:
                print(i + terminating_val)

# my_fun(['41','DROND','GIRIRAJ', '13','ZARA'])
# my_fun(['41','DROND','GIRIRAJ', '13','ZARA'], terminating_val='$')

# my_fun(['41','DROND','GIRIRAJ', '13','ZARA'],terminating_val='$')



# In[40]:


# Variable length positional arguments - 

# def my_fun(a, b, c = 111, *arg):
#     print(arg, type(arg))
#     print(a+b+sum(arg))
#     print(c)
    
# my_fun(10, 20, 30, 40, 50, 60, 70)
# my_fun(10, 20, 50, 30, 40)


# In[48]:


# Variable length Keyworded Arguments
# Values will be stored in dictionary

# def emp_details(e_name, e_id, e_sal, *args, **kwargs):
#     print(kwargs, type(kwargs))
#     print(args, type(args))
#     print(e_name)
#     print(e_id)
#     print(e_sal)
#     print(kwargs['e_city'])

# emp_details('Krishna', 101, 5000)
# emp_details('Krishna', 101, 5000, e_city = 'Bengaluru', e_state = 'Karnataka')


# In[26]:


# Annonymous function - A function without any name
# Using lambda Keyword
# Syntax - lambda parm:expr
# Expr result is the return value
# We don't have to write the return statement explicitly

# (lambda num : True if num%2==0 else False)(4)

# (lambda num:num**(0.5))(4)


a = (lambda num1, num2, num3 : num1 if ((num1>num2) and (num1>num3)) else num2 if (num2>num3) else num3)(12, 100, 99)
print(a)



# In[ ]:


# In Python everything is an object.
# Function is also an object and function is treated as first class citizen in Python.

# filter, map, reduce, sort, 


# In[ ]:


Namespace - Container
Built-in 
Global
Local


# In[51]:


# nonlocal keyword

# def my_fun():
#     a = 10
#     b = 20
#     def inner_fun():
#         nonlocal a
#         a = 11
#         b = 22
#         print(a, b)
#     inner_fun()
#     print(a, b)
# my_fun()


# In[53]:


# global keyword
a = 10
b = 20
def f1():
    global a
    a = 11
    b = 22
    print(a, b)
f1()
print(a, b)


# In[55]:


def f1():
    a = 10
    b = 20
    print(a, b)

def f2():
    x = 11
    y = 22
    print(x, y)


# In[57]:


# Function reference
def f1():
    a = 10
    b = 20
    print(a, b)
    
# f1()
f1


# In[13]:


# Closure - returns another function or inner function

# def f1():
#     a = 111
#     b = 20
#     return a
    
# a1 = f1()
# print(a1)


# def f1():
#     a = 111
#     b = 222
#     return a, b

# f2 = f1
# print(f2)
# print(f1)
# f2()

# def f1():
#     def inner():
#         a = 11
#         b = 22
#         print('Inside inner of f1')
#     return inner
# i1 = f1()
# i1()


# In[15]:


# even_odd(num) -> true if no is even else it will return false

# my_filter(even_odd, lst_num) -> filter the list and gives only list of even numbers

lst = list(range(11,20))

def even_odd(num):
    return True if num%2 == 0 else False


def my_filter(func, lst):
    out_lst = []
    for ele in lst:
        if func(ele):
            out_lst.append(ele)
    return out_lst

my_filter(even_odd, lst)



# In[16]:


get_ipython().run_line_magic('timeit', 'my_filter')


# In[31]:


# filter - used to filter a seq based on some condition
# returns a filter object - which is an iterator
# filter(func, seq/iterable)

lst = list(range(11,20))
list(filter(lambda num: num%2 == 0, lst))



# In[33]:


# map - function is used to map object from one seq to another seq
# returns map object - is also an iterator object
# map(func, iterable)

lst = list(range(11,20))
list(map(lambda num : num**2, lst))


# In[36]:


lst_email = ['abhishek@gmail.com', 'rahul@yahoo.com', 'krishna@hotmail.com', 'kirti@rediffmail.com', 
            'Ram@gmail.com', 'Jagdish@learnbay.co']

# filter the list and return a list of email id where length user name is more than 5

# return a list of usernam for only those email id where length of user name is more than 5


list(filter(lambda email: len(email[:email.index('@')])>5 , lst_email))


list(map(lambda email:email[:email.index('@')], filter(lambda email: len(email[:email.index('@')])>5 , lst_email)))


# In[39]:


lst = [(10,1),(100,2),(23,90),(99,9),(87,7),(67,6),(54,5)]

# sort above list based on last element of the tuple inside the list
lst.sort(key = lambda tpl:tpl[0])
lst


# In[41]:


# reduce - used to find the aggregate values - sum, max, min, product
# import reduce from functools
# reduce(func, seq)
# returns one single aggregate value

# from functools import reduce
# lst = list(range(11,20))
# reduce(lambda x,y : x+y, lst)

# x = 135
# y = 15
# x+y = 50




# In[43]:


print(dir(__builtins__))


# In[44]:


# Iterators & Generators

# Container/Iterable type - list, tuple, set, frozenset, dictionary, byte, bytearray

print(dir(list))


# In[55]:


# Iterable - objects implements __iter__ function

lst = [10,20,30,40]
# print(next(lst))

my_iter = iter(lst)
# print(dir(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# In[49]:


# Iterator object - allows you to iterate over container or iterable object.

# Iterator object implements __iter__ and __next__ function

# zip, enumerate, reversed, filter, map, etc

# print(dir(enumerate))

a = enumerate('Python')
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))



# In[56]:


for i in lst:
    print(i)


# In[69]:


# Syntax of defining generator is similar to function definition

# In the case of geberator we use yield

# yield keyword is similar to return statement

# used to define user defined seq

# generator is efficient in terms of memory and speed both

# import sys
# lst = [i for i in range(10000)]
# print(sys.getsizeof(lst))

# tpl = (i for i in range(10000))
# print(sys.getsizeof(tpl))
# print(next(tpl))
# print(next(tpl))

# lst = [10,20,30,40]


def my_gen():
    a =10
    b = 20
    c = a+b
    yield 10
    yield 10.20
    yield 10+20j
    yield 'Python'
    yield [1,2,3]
    yield True
    
g = my_gen()

for i in g:
    print(i)


# In[ ]:


# Modules in Python

# Any python file(.py) is a module



# In[1]:


print(dir())

import math
print()
print(dir())


# In[4]:


# print(dir(math))

math.sqrt(4)


# In[1]:


# Alternate way

print(dir())
import math as m

print()
print(dir())


# In[3]:


print(m.sqrt(4))

print(math.sqrt(4))


# In[1]:


print(dir())

from math import *
print()
print(dir())


# In[1]:


print(dir())
from math import sqrt, log
print(dir())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




