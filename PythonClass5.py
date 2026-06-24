if syntax
_______

if  condtion:
	if block
	.
	.

a=5
if a>4:
	a=6
print(a)

o/p:
6

a=5
if a<4:
	a=6
print(a)
o/p:
5








#wap take a number from keyboad check no is +ve

print("enter a number ")
no=int(input())
if no>=0:
	print("+ve")

o/p:
enter a number
5
+ve

o/p:
enter a number
-2

#wap take a number from keyboad check no is -ve

print("enter a number ")
no=int(input())
if no<0:
    print("no is -ve ")

#wap take a number from keyboad check no is zero

print("enter a number ")
no=int(input())
if no==0:
    print("zero")

#wap take a number from keyboad check no is nonzero
print("enter a number ")
no=int(input())
if no!=0:
    print("nonzero")

#wap take a number from keyboad check no is even no
print("enter a number ")
no=int(input())
if no%2==0:
    print("even number")



#wap take a number from keyboad check no is odd no
print("enter a number ")
no=int(input())
if no%2!=0:
    print("odd number")


#wap take a number from keyboad check last digit even

print("enter a number ")
no=int(input())
r=no%10
if r%2==0:
    print("last digit even number ")


#wap take a number from keyboad check last digit odd

print("enter a number ")
no=int(input())
r=no%10
if r%2!=0:
    print("last digit odd number ")
#wap take salary from keyboad if salary>=5000 da=30% hra=20% then display basic salary da hra and totalsal

print("enter basic sal ")
sal=float(input())
da,hra=0,0
if sal>=5000:
    da=sal*0.3
    hra=sal*0.2
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",totalsal)


#convert -ve number to +ve number

print("enter a number ")
no=int(input())
if no<0:
    no=-no
print(no)




multiple if
___________________
program contain more than one if evey if condtion must checking


#wap take a number form keyboard check no is 0  +ve -ve

print("enter a number ")
no=int(input())
if no==0:
    print("zero")
if no>0:
    print("+ve")
if no<0:
    print("-ve")


nested if 
_____________

if c1:
    if c2:
        stmt 

#wap take  a number from keyboard check no is 2 digit number  (+ve number )
print("enter a number ")
no=int(input())
if no>9:
    if no<100:
        print("2 digit number ")


#wap take  a number from keyboard check no is 2 digit number  
print("enter a number ")
no=int(input())
if no<0:
    no=-no
if no>9:
    if no<100:
        print("2 digit number ")



#wap take  a number from keyboard check no is 2 digit number 
print("enter a number ")
no=int(input())
if no<0:
    no=-no
if no>9 and no<100:
    print("2 digit number ")

#wap take  a number from keyboard check no is 2 digit number  
print("enter a number ")
no=int(input())
if no<0:
    no=-no
if 9<no<100:
    print("2 digit number ")




ascii   unicode value
________________________
A    65
B    66
Z    90

a    97
b    98
z    122


0    48
1    49
9    57


#display   unicode value of char   or ascii value 
import sys
print("enter a char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
print(ch)
print(ord(ch))

C:\Users\LENOVO\OneDrive\Desktop\python by lipsa>py ifp1.py
enter a char
Z
Z
90

C:\Users\LENOVO\OneDrive\Desktop\python by lipsa>py ifp1.py
enter a char
a
a
97

C:\Users\LENOVO\OneDrive\Desktop\python by lipsa>py ifp1.py
enter a char
z
z
122

C:\Users\LENOVO\OneDrive\Desktop\python by lipsa>py ifp1.py
enter a char
0
0
48

C:\Users\LENOVO\OneDrive\Desktop\python by lipsa>py ifp1.py
enter a char


32



#wap check char is upper case
import sys
print("enter a char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
if ch>='A' and ch<='Z':
    print("upper case")



or

import sys
print("enter a char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
x=ord(ch)
if x>=65 and x<=90:
    print("upper case")


#wap check char is lower case

import sys
print("enter a char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
x=ord(ch)
if x>=97 and x<=122:
    print("lower case")

#wap convert upper case to lower case
import sys
print("enter a upper char ")
ch=input()
if len(ch)!=1:
    print("single char allow ")
    sys.exit()
if ch>='A' and ch<='Z':
        x=ord(ch)+32
        print(chr(x))



if  else  statement
_______________________

if  condtion:
        if stmt block
else:
        else stmt block


if True:
        print("A")
else:
        print("B")


o/p:
A


if False:
        print("A")
else:
        print("B")


o/p:
B



a=5
if a>4:
    a=10
else:
    a=20
print(a)

o/p:
10


a=5
if a<4:
    a=10
else:
    a=20
print(a)

o/p:
20



#wap take a number from keyboard check no is +ve or -ve

print("enter a number ")
no=int(input())
if no>=0:
    print("+ve")
else:
    print("-ve")

#wap take a number from keyboard check no is even or odd
print("enter a number ")
no=int(input())
if no%2==0:
    print("even number")
else:
    print("odd number")

#wap take salary from  keyboad if salary>=5000 da=30% hra=20%  if salary <5000 
da=20% hra=10% then display basic salary da hra and totalsal

print("enter basic sal ")
sal=float(input())
if sal>=5000:
    da=sal*0.3
    hra=sal*0.2
else:
    da=sal*0.2
    hra=sal*0.1
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",totalsal)