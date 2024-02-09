Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Set Methods
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
s1 = {6,8,9,5,3}
s1
{3, 5, 6, 8, 9}
s2 = {1,12,5,8,9,10}
s2
{1, 5, 8, 9, 10, 12}
#1.add
#add() method adds an element to the set. If the element already exists, the add() method does not add the element.
s1.add(10)
s1
{3, 5, 6, 8, 9, 10}
s2.add(10)
s2
{1, 5, 8, 9, 10, 12}
#KeyError not show, If the element already exists.
#--------------------------------------------------
#2.Clear
#clear() method removes all elements in a set.
s1.clear()
s1
set()
#--------------------------------------------------------
#3.Copy
#copy() method copies the set.
x = s2.copy()
x
{1, 5, 8, 9, 10, 12}
id(s2)
2347579672384
id(x)
2347579673504
#return shallow copy set (id diff.).
#------------------------------------------------
#4.Difference
#difference() method returns a set that contains the difference between two sets.
#takes all values from set 1 except common between 2 sets.
s1 = {6,8,9,5,3}
s1
{3, 5, 6, 8, 9}
s2
{1, 5, 8, 9, 10, 12}
s1.difference(s2)
{3, 6}
s2.difference(s1)
{1, 10, 12}
#but what if we want uncommon values from both sets?
#Answer:- symmetric_difference method.
# it returns the all uncommon values from both the sets.
#5.symmetric_difference method
s1.symmetric_difference(s2)
{1, 3, 6, 10, 12}
s1 | s2
{1, 3, 5, 6, 8, 9, 10, 12}
#ignore above operation
#---------------------------------------------------
#6.Difference_update
#difference_update() method removes the items that exist in both sets.
x1 = {1,2,5,6,8}
x1
{1, 2, 5, 6, 8}
x2 = {4,5,7,1,3,2,6}
x2
{1, 2, 3, 4, 5, 6, 7}
x1.difference_update(x2)
x1
{8}
#if we observed the operation is give permanent change in x1.
#difference() method returns a new set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.
#---------------------------------------------
#7.discard()
#discard() method removes the specified item from the set.
y = {1,5,9,99,100}
y
{1, 99, 100, 5, 9}
y.discard(1)
y
{99, 100, 5, 9}
y.discard(111)
y
{99, 100, 5, 9}
#111 is not present in the set but KeyError is not raise.
#This is the differance butween remove() method & discard() method.
#remove() method will raise an error if the specified item does not exist, and the discard() method will   not.
#-------------------------------------------------------
#8.intersection
#Only fetch common elements from the sets.
r1 = {88,33,22,777,22}
r1
{88, 33, 22, 777}
r2 = {33,44,66,88,777,55}
r2
{33, 66, 55, 88, 777, 44}
r1.intersection(r2)
{88, 33, 777}
#-------------------------------------------
#9. intersection_update
#intersection_update() method removes the items that is not present in both sets.
s1 = {11,22,33,44,55}
s1
{33, 22, 55, 11, 44}
s2 = {22,33,66,77,55}
s2
{33, 66, 22, 55, 77}
s1.intersection_update(s2)
s1
{33, 22, 55}
#change in s1 is permanent.
#intersection method create a new set & intersection_update method removes the uncommon items from the original set{11,44}.
#-----------------------------------------------
#10. isdisjoint
x = {"apple", "banana", "cherry"}
x
{'apple', 'cherry', 'banana'}
y = {"google", "microsoft", "facebook"}
y
{'microsoft', 'google', 'facebook'}
x.isdisjoint(y)
True
#isdisjoint() method returns True if none of the items are common in both sets, otherwise it returns False.
x.isdisjoint({'"apple", "banana"})
              
SyntaxError: unterminated string literal (detected at line 1)
x.isdisjoint({"apple", "banana"})
              
False
#both the items are present in x thats why return False.
              
#---------------------------------------------------
              
#11. issubset
              
#issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
              
x
              
{'apple', 'cherry', 'banana'}
x.issubset({'apple','banana'})
              
False
#cherry is missing
              
x = {"a", "b", "c"}
              
y = {"a","b","r","d","c"}
              
x.issubset(y)
              
True
#all the element of x is present in y.
              
#_------------------------------------------------------
              
#12.issuperset
              
help(set.issuperset)
              
Help on method_descriptor:

issuperset(...)
    Report whether this set contains another set.

help(set.issubset)
              
Help on method_descriptor:

issubset(...)
    Report whether another set contains this set.

>>> x
...               
{'a', 'b', 'c'}
>>> y
...               
{'b', 'c', 'd', 'r', 'a'}
>>> x.issuperset(y)
...               
False
>>> x.issubset(y)
...               
True
>>> # issubset y set contain x set completely thats why return true
...               
>>> #issuperset x set not contain y set completely so return False (this(x) set contains another set(y)).
...               
