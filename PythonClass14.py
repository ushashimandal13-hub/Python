operator use list
__________________
[]->index operator
del ->

L=[10,20,30]
print(L[0])
L[1]=25
del L[2]
print(L)

o/P;
10
[10,25]

slicing
___________
[start:stop:step]

L=[10,20,30,40,50,60,70]
del L[2:5:1]
print(L)
o/p:
[10, 20, 60, 70]

L=[10,20,30,40,50,60,70]
L[2:5:1]=[22]
print(L)
o/p:
[10, 20, 22, 60, 70]


L=[10,20,30,40,50,60,70]
L[2:5:1]=[22,25,13]
print(L)

o/p:
[10, 20, 22, 25, 13, 60, 70]


L=[10,20,30,40,50,60,70]
L[5:2:1]=[22,25,13]
print(L)

o/p:
[10, 20, 30, 40, 50, 22, 25, 13, 60, 70]



L=[10,20,30,40,50,60,70]
L[2:2:1]=[22,25,13]
print(L)

o/p:
[10, 20, 22, 25, 13, 30, 40, 50, 60, 70]


L=[10,20,30,40,50,60,70]
del L[2:2:1]
print(L)

o/p:
[10, 20, 30, 40, 50, 60, 70]



L=[10,20,30,40,50,60,70]
L[2:2:1]="hi"
print(L)
o/p:
[10, 20, 'h', 'i', 30, 40, 50, 60, 70]



L=[5,8,12,7,6]
print(7 in L)
print(9 in L)
print(9 not in L)
print([8,12] in L)


o/p:
True
False
True
False

L=[5,8,12]
#print(L+3)error 
print(L*3)

o/p:
[5, 8, 12, 5, 8, 12, 5, 8, 12]

L1 = [10, 20, 30]
L2 = [40, 50]

print(L1 + L2)


o/p:
[10, 20, 30, 40, 50]



L=[10,20]

L += [30,40]

print(L)

o/P
[10, 20, 30, 40]



L=[5,8,12]
L1=[5,8,12]
print(L==L1)
print(L!=L1)

o/p:
True
False


L=[5,8,12]
L1=[5,8,12]
print(L is L1)  #refrence
print(L==L1)   #value

o/p:
False
True



L=[5,7,11,6]
L1=[6,8,11,4]
print(L<L1)
print(L>L1)
print(L<=L1)
print(L>=L1)


o/p:
True
False
True
False
How Python Compares Lists

Python compares the first element of each list.

If they are equal, it compares the second element.

If they are still equal, it compares the third, and so on.

The comparison stops as soon as a difference is found.

L=[5,7,11,6]
L1=[5,8,11,4]
print(L<L1)
print(L>L1)
print(L<=L1)
print(L>=L1)

o/p:
True
False
True
False




keyboard input
__________________


eval():
The eval() function evaluates a string as a Python expression and returns the result.

expression → A string containing a valid Python expression.
Return Value → The result of evaluating the expression.

x=eval("2+3")
print(x)

o/p:
5


print("enter anything")
x=eval(input())
print(type(x))
print(x)


o/p:
enter anything
10
<class 'int'>
10


(1)
L = eval(input("Enter a list: "))
print(L)
print(type(L))

o/p:
Enter a list: [2,4,"hi",8]
[2, 4, 'hi', 8]
<class 'list'>


L =[0,0,0,0,0]
print("enter ",len(L),"elements")
for i in range(len(L)):
	print("enter element ",i+1)
	L[i]=int(input())
print("elemnts are ",L)
o/p:
enter  5 elements
enter element  1
10
enter element  2
20
enter element  3
30
enter element  4
50
enter element  5
60



Q/

enter mark1 
90
enter mark2
80


mark1=90
mark2=80
...
....
total=
avg=



mark =[0,0,0,0]
for i in range(len(mark)):
	print("enter mark ",i+1)
	mark[i]=int(input())
tot=0
for i in range(len(mark)):
	print("mark",i+1,"=",mark[i])
	tot+=mark[i]
print("total mark=",tot)
print("avg mark=",tot/len(mark))


o/p:
enter mark  1
90
enter mark  2
80
enter mark  3
70
enter mark  4
50
mark 1 = 90
mark 2 = 80
mark 3 = 70
mark 4 = 50
total mark= 290
avg mark= 72.5




mark =[0,0,0,0]
for i in range(len(mark)):
	print(f"enter mark{i+1}")
	mark[i]=int(input())
tot=0
for i in range(len(mark)):
	print(f"mark{i+1}={mark[i]}")
	tot+=mark[i]
print("total mark=",tot)
print("avg mark=",tot/len(mark))

o/p:
enter mark1
90
enter mark2
80
enter mark3
70
enter mark4
60
mark1=90
mark2=80
mark3=70
mark4=60
total mark= 300
avg mark= 75.0





L=[]
print("enter how many element store in list ")
size=int(input())
for i in range(0,size,1):
	print("enter element",i+1)
	L.append(eval(input()))
print(L)

enter how many element store in list 
5
enter element 1
10
enter element 2
3
enter element 3
4.5
enter element 4
2+3j
enter element 5
True
[10, 3, 4.5, (2+3j), True]
[Finished in 13.8s]




enter how many element store in list 
4
enter element 1
"hi"
enter element 2
2
enter element 3
3
enter element 4
4
['hi', 2, 3, 4]
[Finished in 8.7s]




L = input("Enter elements: ").split()

print(L)
print(type(L))

Enter elements: 1 2 3 4 5
['1', '2', '3', '4', '5']
<class 'list'>



L = list(map(int, input("Enter numbers: ").split()))

print(L)
print(type(L))
print(L[2]+3)


o/p:
Enter numbers: 1 2 3 4 5
[1, 2, 3, 4, 5]
<class 'list'>
6