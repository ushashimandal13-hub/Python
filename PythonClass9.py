function alias name
_________________
def show():
	print("hi")
s=show
d=s
show()
s()
d()

lambda function or nameless function
_________________________________
one line function  
syntax:
lambda parameter: expression

without lambda
______________
def add(no1,no2):
	return no1+no2
res=add(10,20)
print(res)

using lambda
_____________
res=lambda no1,no2:no1+no2
print(res(2,5))



res=lambda x:x*x
print(res(5))


res=lambda :5
print(res())



call by value  vs call by refeence
__________________________________

any function local variable not recive directly other function .
it must be pass in function parameter.

call by value 
________________

def fun1():
    x = 100
    fun2(x)

def fun2(num):
    print("Value =", num)

fun1()


o/p:
value=100




def fun1():
    x = 100
    print("fun1 x value=",x)
    fun2(x)
    print("fun1 x .. value=",x)

def fun2(num):
    print("fun2 Value =", num)
    num=30
    print("fun2 Value  ...=", num)
fun1()


o/P;
fun1 x value= 100
fun2 Value = 100
fun2 Value  ...= 30
fun1 x .. value= 100
Call by Value (Python)

Python passes object references to functions (often called call by object reference or call by sharing). However, for immutable types like int, float, str, and tuple, it behaves similarly to call by value because the original object cannot be changed.

def change(x):
    x = x + 10
    print("Inside function:", x)

a = 20

change(a)
print("Outside function:", a)


o/p:
Inside function: 30
Outside function: 20


call by refrence  (list ,set,dict,class )
__________________

Call by Reference Concept (Python)
Important Note

Python does not support true Call by Reference like C++.

Python uses Call by Object Reference (Call by Sharing).

Immutable objects (int, float, str, tuple) behave like Call by Value.
Mutable objects (list, dict, set) behave similarly to Call by Reference because changes made inside the function affect the original object.

def change(lst):
    lst[0] = 100
    print("Inside Function :", lst)

numbers = [10, 20, 30]

print("Before Function :", numbers)

change(numbers)

print("After Function :", numbers)


def fun1():
    x=[100]
    print("fun1 x value=",x)
    fun2(x)
    print("fun1 x .. value=",x)

def fun2(num):
    print("fun2 Value =", num)
    num.append(30)
    print("fun2 Value  ...=", num)
fun1()


o/p:
fun1 x value= [100]
fun2 Value = [100]
fun2 Value  ...= [100, 30]
fun1 x .. value= [100, 30]




Summary Table
Object Type	Mutable?	Original Changes?	Behavior
int	❌ No	❌ No								Like Call by Value
float	❌ No	❌ No							Like Call by Value
str	❌ No	❌ No	                        Like Call by Value
tuple	❌ No	❌ No	                      Like Call by Value
list	✅ Yes	✅ Yes	                   Like Call by Reference
dict	✅ Yes	✅ Yes	                  Like Call by Reference
set	✅ Yes	✅ Yes	                      Like Call by Reference



module
__________
it is a python file.
inside file we write variable,function,class and other,....
(a)predefined module
example  sys,numpy,panda,.....
(b)userdefined module
  programer created 
  that name must be valid identifier

How to acess module 
____________________
(1)import modulename
(2)import modulename as duplicatename
(3)from modulename import memeber,memeber,...
(4)from modulenme import *


mymodule.py
_____________
def add(no1,no2):
	return no1+no2
def show():
	print("show function")
a=10


first.py
____________
import mymodule
mymodule.show()
print(mymodule.a)
print(mymodule.add(10,20))


second.py
____________
import mymodule as m
m.show()
print(m.a)
print(m.add(10,20))

third.py
____________
from mymodule import show,a,add
show()
print(a)
print(add(10,20))

four.py
__________
from mymodule import *
show()
print(a)
print(add(10,20))

import math as m
print(m.sqrt(16))
print(m.pi)




import math

print(dir(math))


o/p:
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
[Finished in 89ms]


import math

print(len(dir(math)))

o/p:
66


How to see one module contain how many function,...
__________________________
import mymodule 
print(help(mymodule))

o/P;
Help on module mymodule:

NAME
DATA
    a = 10
FILE
    c:\users\lenovo\onedrive\desktop\adityapython+2\mymodule.py

None



import math
help(math.sqrt)


o/p:
Help on built-in function sqrt in module math:

sqrt(x, /)
    Return the square root of x.


How to install third party module
_____________________________

syntax:

pip  install  modulename/packagename


pip install  numpy



syntax:
how to uninstall
___________________

pip uninstall  modulename/packagename

pip unistall  numpy




import random as r
x=r.random()
print(x)
print(round(x,2))
print(r.uniform(10,20))
print(r.randrange(10,20))
print(r.choice("hello"))
print(r.choice([3,5,7,9,12]))
print(r.sample("hello",2))
print(r.sample([3,5,7,9,12],3))


o/p:
0.4822208084998769
0.48
16.859137643433044
17
l
7
['l', 'o']
[12, 5, 9]