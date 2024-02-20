""""""
"""
Higher Order functions:
Higher-order functions are functions that take a function as a parameter
Apply that input function over the sequence and generates a result
These functions are Higher order functions.
function(input_function,sequence/iterable)
input_function:- normal function/lambda
iterable:-collection of elements Ex. tuple,set,list,string,dict etc.
Higher order functions are of 3 types:
1. filter function
2. map function
3. reduce function
========================================
1. filter function
The filter() method filters the given sequence with the help of based on condition specified
in an input function that tests each element in the sequence to be true or not.
Syntax:
filter(function,iterable) #its condition based
# filter only EVEN numbers from a sequence x
x = [10,22,34,56,67,79,97,277]
evn = lambda num:num%2==0 #eve is input function
print(evn)
#output:-<function <lambda> at 0x0000016C6B053E20>
#by using type casting we get the list
print(list(filter(evn,x)))
#output:-[10, 22, 34, 56]
-----------------------------------
# filter only divisible by 5 numbers from a sequence x
x = [10,22,34,56,67,79,97,277]
divi_5 = filter(lambda num:num%5==0,x)
print(list(divi_5))
#output:- [10]
----------------------------------------
#fetch name whose len is >5 character
nm = ['nanda','rohidas','swapnil','pooja','ankush']
nm_l5 = filter(lambda name:len(name)>5,nm)
print(list(nm_l5))
#output:- ['rohidas', 'swapnil', 'ankush']
=================================================
2. map function:-function returns a map object(which is an iterator) of the results 
after applying the given function to each item of a given iterable (list, tuple etc.),
hence its operation/expression based.
Syntax:
map(func,iter)
-----------------------------
# We double all numbers using map()
numbers = (1, 2, 3, 4)
num_add = map(lambda num:num+num,numbers)
print(list(num_add))
#output:- [2, 4, 6, 8]
--------------------------------
#Write a Python program to add two given lists and 
find the difference between them. Use the map() function.
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
result = map(lambda x,y:(x+y,x-y),nums1,nums2)
print(list(result))
output:-
[(6, 6), (6, 4), (10, -4), (16, 2)]
==========================================
3. reduce function:-
-reduce function is use to reduce a sequence into a single output & its not builtin function.
-it is present in functools module so we need to import reduce from functools.
------------------------------------ 
#Write a Python function to sum all the numbers in a list.
from functools import reduce #by using this line we import reduce
x = (8,2,3,0,7)
add_x = lambda x,y:x+y
print(reduce(add_x,x))
#output:- 20
----------------------------------
#find out max num from a
a = [12,8,66,40,3,120]
from functools import reduce
y = reduce(lambda num1,num2:num1 if num1>num2 else num2,a)
print(y)
output:- 120
----------------------------
"""



