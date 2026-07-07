List:
it a predefined datastructre.
it is collection of simliar and dismliar elements.
it is mutable.
inserorder is preseved
index and slicing concept avaliable
duplicate elememt allow .
[] to create list

L=[]
print(type(L))

o/p:
<class list>

L=[]
L.append(10)
L.append(20)
L.append(30)
print(L)

o/p:
[10,20,30]


L=[]
L[0]=10
print(L)

o/p:
error


L=[]
L.append(5)
L[0]=10
#L[1]=20 error
print(L)

o/p:
10


L=[10,20,30]

print(L)

o/p:
[10,20,30]


L=[10,"hi",3.5,True]

print(L)

o/P;
[10, 'hi', 3.5, True]

string convert to list
______________________
a="hello"
L=list(a)
print(L)

o/p:
['h', 'e', 'l', 'l', 'o']


s="ram is a good boy"
L=s.split()
print(L)

o/p:
['ram', 'is', 'a', 'good', 'boy']


predefined function list
_____________________
L=[10,20,30,40]
L.append(50)
print(L)

o/p:
[10, 20, 30, 40, 50]

insert()
_____________
L=[10,20,30,40]
L.insert(1,50)
print(L)

L=[10,20,30,40]
L.extend("hi")
print(L)

o/P;
[10, 20, 30, 40, 'h', 'i']
L=[10,20,30,40]
L.insert(1,"hi")
print(L)

[10, 'hi', 20, 30, 40]







remove()
___________
L=[10,20,30,40,20]
L.remove(20)
print(L)

o/P;
[10, 30, 40, 20]

pop():
L=[10,20,30,40,20]
L.pop()
print(L)
o/P;
[10, 20, 30, 40]


L=[10,20,30,40,20]
L.pop(2)
print(L)
o/p:
[10, 20, 40, 20]

clear():
__________
L=[10,20,30,40,20]
L.clear()
print(L)

sort():
__________
L=[5,9,8,12,6]
L.sort()
print(L)


reverse()
________________
L=[5,9,8,12,6]
L.reverse()
print(L)


L=[5,9,8,12,6]
L.sort(reverse=True)
print(L)

o/P;
[12,9,8,6,5]



L=[5,9,8,12,6,8]
print(L.index(8))
print(L.count(8))
L1=L.copy()
print(L1)
L1.pop()
print(L)
print(L1)





append
insert
extend
pop
remove
clear
sort
reverse
index
count
copy