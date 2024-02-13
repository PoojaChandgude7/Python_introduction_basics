""""""
"""
Flow Control blocks
1. Conditional or selective statement
if <condition>
if else
if elif else
if elif elif .... else
========================================
2.Iterative statements
1. for loop
2. while loop
---------------
for loop: is used to fetch elements from an iterable 
one by one

Iterables in python- list,set,tuple,dict,str,range
----------------------------------
Q. fetch vowals from give string.
sentence = input('Enter the sentence:-')
sent_lower = sentence.lower()
v = ['a','e','i','o','u']
count = 0
for i in sent_lower:
    if i in v:
        count = count + 1
print('Total vowles in sentence:-', count)
--------------------------------------------
for i in range(2,101,2):
    print(i,end=" ")
----------------------------------
number1 = 20
number2 = 30
product = number1 * number2
if product<= 1000:
    print(product)
else:
    print(number1 + number2)
-------------------------------
Q.Write a program to iterate the first 10 numbers, and in each iteration,
print the sum of the current and previous number.
print("Printing current and previous number and their sum in a range(10)")
pri_num = 0
for i in range(0,11):
    x_sum = pri_num + i
    print("current no.:-",i,'and previous no.:-',pri_num,'and their sum:-',x_sum)
    # but the previous no. is show in every code is 0
    # that's why we put
    pri_num = i
-------------------------------------
#Q.Print characters from a string that are present at an even index number.
x = input('Enter your string:-')
y = list(x)
#print(y)
size = len(y)
#print (size)

for i in range(0,size-1,2):
    print("index[",i,"]", x[i])
Ans:- Enter your string:-Good Morning Pune
index[ 0 ] G
index[ 2 ] o
index[ 4 ]  
index[ 6 ] o
index[ 8 ] n
index[ 10 ] n
index[ 12 ]  
index[ 14 ] u
or by using slicing
for i in y[0::2]:
    print(i)
-----------------------------------------------
#.Q Check if the first and last number of a list is the same
numbers_x = [10, 20, 30, 40, 10]

if numbers_x[0] == numbers_x[4]:
    print('True')
else:
    print('False')
-------------------------------
"""






















































































































