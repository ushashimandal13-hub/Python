looping
_________________
some statement repeated continously then you choose loop.


print("hi")
print("hi")
print("hi")
print("hi")
print("hi")



print("A")
print("B")
print("C")
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")



i=1
print(i)
i=i+1
print(i)
i=i+1
print(i)
i=i+1
print(i)
i=i+1
print(i)
i=i+1


using looping we write that repeated stmt only once inside the loop body part


There are 2 types
(1)while
(2)for in

every loop there are 3 section
(1)start value /initlization
(2)stop value /condtion
(3)step value /update /inc/dec

while loop syntax
____________________

initlization
while condtion:
	repeated stmt write once
	inc/dec


#wap display hi msg 5 times

i=1
while i<6:
	print("hi")
	i=i+1  #i+=1


#wap display A B C 3 times

i=1
while i<4:
	print("A")
	print("B")
	print("C")
	i=i+1
#wap display 1 to 5
i=1
while i<6:       #i<=5    #i!=6
	print(i)
	i=i+1

#wap display 10 to 20
i=10
while i<21:   #i<=20   #i!=21
	print(i)
	i=i+1

#wap display 5 to 1
i=5
while i>0:    # i>=1     #i!=0 
	print(i)
	i=i-1
#wap display 20 to 10
i=20
while i>9:   #i!=9  #i>=10
	print(i)
	i=i-1


print("A")
i=1
while i<5:
	print("B")
	i=i+1
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
C
B
C
D
5

continue:
it is keyword.
it is used to continue the loop .
every language every loop last statement continue.

print("A")
i=1
while i<5:
	print("B")
	i=i+1
	print("C")
	continue #by default
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
B
C
D
5




print("A")
i=1
while i<5:
	print("B")
	i=i+1
	continue
	print("C")
print("D")
print(i)

i=1,2,3,4,5
o/p:
A
B
B
B
B
D
5




print("A")
i=1
while i<5:
	print("B")
	i=i+1
	if i>=3:
		continue
	print("C")
print("D")
print(i)

i=1,2,3,4,5
o/p:
A
B
C
B
B
B
D
5





break:
it is keyword.
it is used stop the loop .

print("A")
i=1
while i<5:
	print("B")
	i=i+1
	print("C")
	break
print("D")
print(i)
o/p:
A
B
C
D
2



print("A")
i=1
while i<5:
	print("B")
	i=i+1
	break
	print("C")
print("D")
print(i)

i=1,2
o/p:
A
B
D
2




print("A")
i=1
while i<5:
	print("B")
	i=i+1
	if i>=3:
		break
	print("C")
print("D")
print(i)

i=1,2,3
o/p:
A
B
C
B
D
3