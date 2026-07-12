array  in python  
_____________
Using the array Module

The array module stores only elements of the same type.


from array import array

arr = array('i', [1, 2, 3, 4, 5])  # 'i' means integer

print(arr)

arr.append(6)
print(arr)

print(arr[2])  # Access element




from array import array

a = array('f', [3.141592653589793])
b = array('d', [3.141592653589793])

print(a)
print(b)


from array import array
arr = array('i', [1, 2, 3, 4, 5])  # 'i' means integer
print(arr)
arr.append(6)
print(arr)
print(arr[2])  # Access element


Here, 'i' means the array can store only integers.

Common Type Codes
Type Code	Data Type	Size (Typical)	Example
'b'	Signed Character	1 byte	array('b', [10, -5])
'B'	Unsigned Character	1 byte	array('B', [10, 255])
'h'	Signed Short Integer	2 bytes	array('h', [1000, -200])
'H'	Unsigned Short Integer	2 bytes	array('H', [1000, 5000])
'i'	Signed Integer	Usually 4 bytes	array('i', [10, 20, 30])
'I'	Unsigned Integer	Usually 4 bytes	array('I', [10, 20, 30])
'l'	Signed Long Integer	4 or 8 bytes	array('l', [100000])
'L'	Unsigned Long Integer	4 or 8 bytes	array('L', [100000])
'q'	Signed Long Long Integer	8 bytes	array('q', [123456789])
'Q'	Unsigned Long Long Integer	8 bytes	array('Q', [123456789])
'f'	Float	4 bytes	array('f', [1.2, 2.5])
'd'	Double (Double-precision Float)	8 bytes	array('d', [1.23456789, 2.3456789])
'u'*	Unicode Character (deprecated)	Platform dependent	array('u', 'ABC')

Note: The 'u' type code is deprecated in recent Python versions. Use strings or Unicode libraries instead.





arr = ['H', 'E', 'L', 'L', 'O']

print(arr)



text = "HELLO"

arr = list(text)

print(arr)



all method list that work in array
___________________________________
append()
insert()
extend()
pop()
remove()
....
...



https://chatgpt.com/share/6a50e677-cb94-83ee-9505-b02c7cafb781


2d array using array module
________________________- 

The Python array module does not support 2D arrays directly. It only supports one-dimensional (1D) arrays.

However, you can create a 2D array by using a list of array objects.



from array import array

arr = [
    array('i', [10, 20, 30]),
    array('i', [40, 50, 60]),
    array('i', [70, 80, 90])
]

print(arr)


o/p:
[array('i', [10, 20, 30]), array('i', [40, 50, 60]), array('i', [70, 80, 90])]





from array import array

arr = [
    array('i', [10, 20, 30]),
    array('i', [40, 50, 60]),
    array('i', [70, 80, 90])
]

print(arr[0][0])
print(arr[1][2])
print(arr[2][1])






from array import array

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

matrix = []

for i in range(r):
    row = array('i')
    for j in range(c):
        x = int(input(f"Enter element [{i}][{j}]: "))
        row.append(x)
    matrix.append(row)

print("\nMatrix:")

for row in matrix:
    print(*row)


How to use numpy
__________________
first install command prompt

pip install numpy



import numpy as np
matrix = np.array([[1, 2],[3, 4]])
print(matrix)


o/p:
[[1 2]
 [3 4]]



without numpy
________________
L=[10,20,30,40]
L2=[]

for i in L:
    L2.append(i*2)

print(L2)

o/p:
[20, 40, 60, 80]

Using NumPy


import numpy as np
a=np.array([10,20,30,40])
print(a*2)

o/p:
[20, 40, 60, 80]



a=np.array([10,20,30])
print(type(a))

o/p:
<class 'numpy.ndarray'>


a=np.array([1,2,3])
print(a)



a=np.zeros(5)
print(a)

[0. 0. 0. 0. 0.]




a=np.ones(5)
print(a)

[1. 1. 1. 1. 1.]





import numpy as np
a=np.empty(5)
print(a)


[1.38501008e+219 9.08669059e+223 3.68069869e+180 1.76916719e-312
 0.00000000e+000]




a=np.arange(1,11)

print(a)

o/p:
[1 2 3 4 5 6 7 8 9 10]



import numpy as np

a = np.linspace(1, 10, 5)

print(a)