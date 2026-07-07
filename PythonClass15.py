List Comprehension in Python

List Comprehension is a short and elegant way to create a list in Python using a single line of code.

Syntax
new_list = [expression for item in iterable if condition]
expression → Value to add to the new list.
item → Current element.
iterable → List, tuple, string, range(), etc.
condition → Optional filter.


without using  List Comprehension
___________________________________
#one list store another list using sequence concept

L=[2,5,8,7]
L1=[]
for i in L:
	L1.append(i)
print(L1)

o/p:
[2, 5, 8, 7]


#one list store another list using index concept
L=[2,5,8,7]
L1=[]
for i in range(0,len(L),1):
	L1.append(L[i])
print(L1)



using list comphersion
_____________________

#one list store another list using sequence concept

L=[2,5,8,7]
L1=[i for i in L]
print(L1)

o/p:
[2, 5, 8, 7]

or

L=[2,5,8,7]
L1=[L[i] for i in range(0,len(L),1)]
print(L1)

o/p:
[2, 5, 8, 7]





without using  List Comprehension
___________________________________
#one list even data store another list using sequence concept

L=[2,5,8,7]
L1=[]
for i in L:
	if i%2==0:
		L1.append(i)
print(L1)

o/p:
[2,8]

using  List Comprehension
______________________
L=[2,5,8,7]
L1=[i for i in L if i%2==0]
print(L1)

o/p:
[2,8]


L=[3,6,8,9,2,1,7]
L1=[i for i in L if i>5]
print(L1)

o/p:
[6, 8, 9, 7]








without using list comphersion
______________________________
L=[3,6,8,9,2,1,7]
L1=[]
for i in L:
	if i>5:
		if i%2==0:
			L1.append(i)
print(L1)

o/p:
[6, 8]

using list comphersion
_______________________
L=[3,6,8,9,2,1,7]
L1=[i for i in L if i>5 and i%2==0]
print(L1)

o/p:
[6,8]




L=[3,6,8,9,2,1,7]
L1 = [i for i in L if i > 5 if i % 2 == 0]
print(L1)


o/p:
[6,8]





L=[3,6,8,9,2,1,7]
L1 = [i if i > 5 and i % 2 == 0 else 0 for i in L]
print(L1)

o/p:
[0, 6, 8, 0, 0, 0, 0]



no=5
if no>0:
	print("+ve")
else:
	print("-ve")


ternary operatory
________________
syn:
truepart if condtion else falsepart
example:
print("enter a no ")
no=int(input())
print("+ve") if no>0 else print("-ve")





number 2 divide True  not divide false add  new list without list comhersion
_____________________________________________
L=[3,6,8,9,2,1,7]
L1=[]
for i in L:
	if i%2==0:
		L1.append(True)
	else:
		L1.append(False)
print(L1)

o/p:
[False, True, True, False, True, False, False]


using list comhersion
_____________________

L=[3,6,8,9,2,1,7]
L1=[True if i%2==0 else False for i in L]
print(L1)

o/p:
[False, True, True, False, True, False, False]


L=[3,6,8,9,2,1,7]
L1=[]
for i in L:
	if i>5:
		if i%2==0:
			L1.append(i+3)
		else:
			L1.append(i-2)
print(L1)

o/p:
[9,11,7,5]


L=[3,6,8,9,2,1,7]
L1=[i+3 if i%2==0 else i-2 for i in L if i>5]
print(L1)
o/p:
[9,11,7,5]


L1=[i for i in range(5)]
print(L1)

o/p:
[0, 1, 2, 3, 4]


L1=[i for i in "hello"]
print(L1)

o/p:
['h', 'e', 'l', 'l', 'o']


L1=[i for i in "hello" if i in "aeiouAEIOU"]
print(L1)
o/p:
['e','o']