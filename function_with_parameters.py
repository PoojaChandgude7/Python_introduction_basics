""""""
"""
Function with parameters/arguments
There 4 types
- Positional Arguments
- Keyword args.
- default args.
- Variable length args
====================================
Types of arguments:
1. Positional arguments: Its follows sequence order
Example:
def name(student_name,age,place):
    print("student_name:-",student_name)
    print("age:-",age)
    print("place:-",place)
name("Tanaji",20,"Satara")
output:-
student_name:- Tanaji
age:- 20
place:- Satara
----------------------------
name(20,"Satara","Tanaji")
output:-
student_name:- 20
age:- Satara
place:- Tanaji
# in above result is false because the positional arg
# are not following a sequence
=====================================================
2. Keyword argument:here sequence doesnt matter because we 
give a reference with args/parameters
Example:
def name(student_name,age,place):
    print("student_name:-",student_name)
    print("age:-",age)
    print("place:-",place)
name(age=20,place="Satara",student_name="Tanaji")
#we are taking help of arg to allocate values 
and we get the right result.
output:-
student_name:- Tanaji
age:- 20
place:- Satara
=====================================================
3. Default argument:-
we can set a value as a default value then the missing value itself 
fill by default value.
Example:- 
def name(student_name="Pooja",age="29",place="Pune"):
   print(student_name,age,place)

name("Swapnil","30")
output:-
output:-
Swapnil 30 Pune #by defult it take place pune
--------------
def show(x,y,z=23):
    print(x,y,z)

show(10,20,30)
------------------
def num(z=23,x,y):
    print(x,y,z)

num(10,20,30)
output:-
SyntaxError: non-default argument follows default argument
so we must gave 1st non default arg and then known default argument
"""





