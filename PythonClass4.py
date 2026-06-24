range(start,stop,step)
range(start,stop)
range(stop) start=0 stop-1,1


for element in sequence:
	repeated stmt

sequence
_____________
list
tuple
set
dict
range
string

for i in "bye":
	print(i)

o/P:
b
y
e

for i in "bye":
	print("hi")

o/P:
hi
hi
hi


for i in [1,5,7,9]:
	print(i)

o/p:
1
5
7
9

display 1 to 10

for i in range(1,11,1):
	print(i)

o/P;
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

for i in range(1,11):
	print(i)

o/P:
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


for i in range(11):
	print(i)

o/P:
0
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

for i in range(3):
	print(i)

o/p:
0
1
2

for i in range(0,3,1):
	print(i)



for i in range(3):
	print("i")

o/p:
i
i
i

for i in range(5):
	print("hi")


o/P:
hi
hi
hi
hi
hi


break:
it is used to stop the loop

print("A")
for i in range(3):
	print("B")
	break
	print("C")
print("D")
print(i)




o/p:
A
B
D
0

rint("A")
for i in range(3):
	print("B")
	if i==2:
		break
	print("C")
print("D")
print(i)

o/p:
A
B
C
B
C
B
D
2


for i in [3,6,5,7,12,8]:
	if i==7:
		break
	print(i)

o/p:
3
6
5


for i in range(5):
	if i==2:
		break
	print(i)

o/p:
0
1



continue:
it is used to continue the loop
every loop last statment by default continue
print("A")
for i in range(3):
	print("B")
	print("C")
	continue
print("D")
print(i)

o/p:
A
B
C
B
C
B
C
D
2


for i in range(3):
	print("B")
	continue
	print("C")
print("D")
print(i)

o/P
B
B
B
D
2


print("A")
for i in range(3):
	print("B")
	if i==1:
		continue
	print("C")
print("D")
print(i)

o/p;
A
B
C
B
B
C
D
2





for i in [3,6,5,7,12,8]:
	if i==7:
		continue
	print(i)

o/p:
3
6
5
12
8



for i in range(5):
	if i==2:
		continue
	print(i)

o/p:
0
1
3
4

pass:

for i in range(3):
	pass
print(i)

o/P;
2



for i in range(3):
	print("A")
else:
	print("B")
print(i)


o/P;
A
A
A
B
2



for i in range(3):
	print("A")
	break
else:
	print("B")
print(i)

o/P;
A
0