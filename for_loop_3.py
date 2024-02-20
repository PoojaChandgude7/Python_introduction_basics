"""
Q.fetch keys from dict.
x = {'mob1':'motorola','mob2':'MI','mob3':'samsung'}
for i in x:#by default give key's
    print(i)
Soln:-mob1
mob2
mob3
=====================================
x = {'mob1':'motorola','mob2':'MI','mob3':'samsung'}
for i in x: #its give both key's
    print(i,x[i]) #(key's,values)
Soln:-
mob1 motorola
mob2 MI
mob3 samsung
=================================
x = {'mob1':'motorola','mob2':'MI','mob3':'samsung'}
for i in x.values():#its give both values or use x.items()
    print(i)
Soln:-
motorola
MI
samsung
=============================================
Patterns programs
*
**
***
****
*****
for i in range(6):
    print(i*"*")
====================================
*****
****
***
**
*
for i in range(5,0,-1):
    print(i*'*')
=======================================
 *  *  *  *  *
 *  *  *  *
 *  *  *
 *  *
 *
for i in range(5,0,-1):
    print(i*' * ')
===============================
Q. print 1 to 100 by using for loop
for i in range(1,101):
    print(i, end=" ")
=================================
Q.print 1 to 100 by using for while loop
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
===============================
Q. print multiplication program using for loop
num = int(input("Enter the number for multiplication table:-"))
print ("The Multiplication Table of:-",num)
for i in range(1, 11):
   print (num,'x',i, '=',num * i)
Soln:-
Enter the number for multiplication table:-9
The Multiplication Table of:- 9
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
===============================
Q. print 1 to 10 multiplication tables.
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
Soln:-
1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
=========================================
A
BB
CCC
DDDD
EEEEE
chr(): chr() function takes integer argument and give a num
       return the string representing a character at that code point.
Example:-
y = chr(65)
print(y)
Soln:- A
ord(): function takes string argument of a single Unicode character and
       return its integer Unicode code point value.
Example:-
x = ord('A')
print(x)
Soln:-
65
================================
A A A A A A
B B B B B B
C C C C C C
D D D D D D
for i in range(4):#work on row
    for j in range(6):#work on column
        print(chr(65+i), end=" ")
    print()
======================================
A B C D E F
A B C D E F
A B C D E F
A B C D E F
for i in range(4):
    for j in range(6):
        print(chr(65+j),end=" ")
    print()
=======================================
for i in range(4):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,4):
        print(chr(65+i),end="")
    print()
Soln:-
AAAA
 BBB
  CC
   D
==============================
"""