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

nested list
_______________
L=[3,7,[5,6],9]
print(L[1])
print(L[2])
print(L[3])

o/p:
7
[5, 6]
9


L=[[1,2,3],[4,5,6],[7,8,9]]

print(L)
print(L[0])
print(L[0][1])
print(L[2][2])


o/p:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3]
2
9

sequence
_____________

L=[[1,2,3],[4,5,6],[7,8,9]]
for i in L:
	print(i)
o/P:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

L=[[1,2,3],[4,5,6],[7,8,9]]
for i in L:
	for j in i:
		print(j,end="\t")
	print()

o/p:
1	2	3	
4	5	6	
7	8	9	


range
__________
L=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(L),1):
	print(L[i])

[1, 2, 3]
[4, 5, 6]
[7, 8, 9]



L=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
			print(L[i][j],end="\t")
	print()

1	2	3	
4	5	6	
7	8	9


sum of all element in list
______________________________

L=[[1,2,3],[4,5,6],[7,8,9]]
s=0
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
			s=s+L[i][j]
print("sum of all element=",s)

o/p:
sum of all element= 45



nested list list comphersion:
_____________________________
L=[[1,2,3],[4,5,6],[7,8,9]]
L1=L[::1]

print(L1)

o/P:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[]
for i in L:
	L1.append(i)
print(L1)

o/P:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]




without using comphersion
L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[]
for i in L:
	x=[]
	for j in i:
		x.append(j)
	L1.append(x)
print(L1)

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]





L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[]
for i in range(0,len(L),1):
	x=[]
	for j in range(0,len(L[i]),1):
		x.append(L[i][j])
	L1.append(x)
print(L1)

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]



L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[[j for j in i]for i in L]
print(L1)

o/p:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]


L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[[j+2 for j in i]for i in L]
print(L1)

o/P:
[[3, 4, 5], [6, 7, 8], [9, 10, 11]]


L=[[1,2,3],[4,5,6],[7,8,9]]
L1=[[j for j in i if j%2==0]for i in L]
print(L1)

o/p:
[[2], [4, 6], [8]]



A=[[1,2,3],[4,5,6]]
B=[[2,3,4],[1,5,2]]
C=[]
C=A+B
print(C)

o/p:
[[1, 2, 3], [4, 5, 6], [2, 3, 4], [1, 5, 2]]


list matrix addition
_______________________
A=[[1,2,3],[4,5,6]]
B=[[2,3,4],[1,5,2]]
C=[]
for i in range(0,len(A),1):
	X=[]
	for j in range(0,len(A[i]),1):
		X.append(A[i][j]+B[i][j])
	C.append(X)	
print(C)

o/p;
[[3, 5, 7], [5, 10, 8]]


matriax addition using list comphersion
____________________________________
A=[[1,2,3],[4,5,6]]
B=[[2,3,4],[1,5,2]]
C=[[A[i][j]+B[i][j] for j in range(0,len(A[i]),1) ]for i in range(0,len(A),1) ]

print(C)




upper traingle
lower traingle
transpose matrix
mult