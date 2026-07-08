nested list
___________
L=[[1,7,3],[4,8,6]]
print(L)
print(L[0])
print(L[1])
print(L[0][1])
print(L[1][2])

[[1, 7, 3], [4, 8, 6]]
[1, 7, 3]
[4, 8, 6]
7
6


display nested list matrix format
____________________________________
L=[[1,7,3],[4,8,6]]
for i in L:
	print(i)

o/p:
[1, 7, 3]
[4, 8, 6]



L=[[1,7,3],[4,8,6]]
for i in L:
	for j in i:
		print(j,end="\t")
	print()


o/p:
1       7       3
4       8       6



2nd way
____________


L=[[1,7,3],[4,8,6]]
for i in range(0,len(L),1):
	print(L[i])
o/p:
[1, 7, 3]
[4, 8, 6]

another way
_______________

L=[[1,7,3],[4,8,6]]
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()


o/p:
1       7       3
4       8       6




#take input from keyboard
print("enter collection of list ")
L=eval(input())
print("list data ")
print(L)
C:\Users\DELL\Desktop\pythonprogram>py 1.py
enter collection of list
[[1,2,3],[4,5],[6]]
list data
[[1, 2, 3], [4, 5], [6]]


L=[]
print("enter how many list store ")
r=int(input())
for i in range(r):
	print("enter list",i+1," data")
	L.append(eval(input()))
print("elements are ")
print(L)
C:\Users\DELL\Desktop\pythonprogram>py 1.py
enter how many list store
2
enter list 1  data
[10,20,30]
enter list 2  data
[40,50]
elements are
[[10, 20, 30], [40, 50]]




L=[]
print("enter list r and c ")
r=int(input())
c=int(input())
print("enter ",r*c,"elements")
for i in range(r):
	x=[]
	for j in range(c):
		x.append(int(input()))
	L.append(x)
print("elements are ")
print(L)
C:\Users\DELL\Desktop\pythonprogram>py 1.py
enter list r and c
3
4
enter  12 elements
1
2
3
4
5
6
7
8
9
10
11
12
elements are
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]





L=[]
print("enter how many  list store ")
r=int(input())
for i in range(r):
	x=[]
	print("list ",i+1," store how many data")
	c=int(input())
	for j in range(c):
		print("enter data ",j+1)
		x.append(int(input()))
	L.append(x)
print("elements are ")
print(L)
:\Users\DELL\Desktop\pythonprogram>py 1.py
enter how many  list store
3
list  1  store how many data
4
enter data  1
10
enter data  2
20
enter data  3
30
enter data  4
40
list  2  store how many data
2
enter data  1
30
enter data  2
40
list  3  store how many data
1
enter data  1
70
elements are
[[10, 20, 30, 40], [30, 40], [70]]





L=[[0,0,0],[0,0]]

for i in range(len(L)):
	for j in range(len(L[i])):
		print("enter list",i+1,"data ",j+1)
		L[i][j]=int(input())
print("elements are ")
print(L)
C:\Users\DELL\Desktop\pythonprogram>py 1.py
enter list 1 data  1
10
enter list 1 data  2
20
enter list 1 data  3
30
enter list 2 data  1
40
enter list 2 data  2
50
elements are
[[10, 20, 30], [40, 50]]