loop:
_______
some statement repeated continously then choose loop
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")


for i in range(3):
	print("A")
	print("B")
	print("C")

function
_____________
some statement repated after some time then choose  function

print("A")
print("B")
print("C")
print("D")
print("A")
print("B")
print("C")
print("E")
print("A")
print("B")
print("C")
print("F")

solve these program using function
_______________________________

def  show():
	print("A")
	print("B")
	print("C")
	return
show()
print("D")
show()
print("E")
show()
print("F")

How to define function
________________

syntax or rule
________________

def  functionname(formal parameter or argument):
	local variable
	logic
	return 

How to call function
____________________

functionname(actual parameter /argument)


we can write function program 4 way
________________________________

(1)no return value no argument
(2)no return value with argument
(3)return value with no argument
(4)return value with argument


# add of two no from keyboard
print("enter a number")
no1=int(input())
print("enter another number")
no2=int(input())
s=no1+no2
print("sum=",s)

(1)no return value no argumnet
def add():
	print("enter a number")
	no1=int(input())
	print("enter another number")
	no2=int(input())
	s=no1+no2
	print("sum=",s)
	return
add()

(2)even or odd using function no return value no argument
def check():
	print("enter a number ")
	no=int(input())
	if no%2==0:
		print("even number ")
	else:
		print("odd number")
check()

(3)find simple interset using function no return value no argument
sical()


def  sical():
	print("enter priniple")
	p=float(input())
	print("enter rate of interset")
	r=float(input())
	print("enter time")
	t=float(input())
	si=p*r*t/100
	print("simple interset=",si)
sical()


(2)no return value with argument

def add(no1,no2):
	s=no1+no2
	print("sum=",s)
add(10,20)





def add(no1,no2):
	s=no1+no2
	print("sum=",s)
print("enter a nnumber")
no1=int(input())
print("enter another number")
no2=int(input())
add(no1,no2)


def check(no):
	if no%2==0:
		print(no,"is even number ")
	else:
		print(no,"is odd number ")
print("enter a nnumber")
no=int(input())
check(no)

def sical(p,r,t):
	si=p*r*t/100
	print("simple interset=",si)
	return 
print("enter priniple")
p=float(input())
print("enter rate of interset")
r=float(input())
print("enter time")
t=float(input())
sical(p,r,t)



return value with no argument
______________________________
def add():
	print("enter a number ")
	no1=int(input(())
	print("enter another number ")
	no2=int(input())
	s=no1+no2
	return s
res=add()
print("sum of two no=",res)

evenodd
sical

return value with argument
______________________________
def add(no1,no2):
	s=no1+no2
	return s
print("enter a number ")
no1=int(input(())
print("enter another number ")
no2=int(input())
res=add(no1,no2)
print("sum of two no=",res)


evenodd
sical

why function final 
____________________


1!+2!+3!+4!+5!=155


3!  3*2*1
5!  5 *4*3*2*1

1! 1
0!  1

no=5
f=1
while no>0:
	f=f*no
	no=no-1
print("factorial=",f)






no=5
f=1
s=0
while no>0:
	f=f*no
	no=no-1
s=s+f
no=4
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
no=3
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
no=2
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
no=1
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
print("first 5 factorial sum=",s)


slove using function
__________________

def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=facttest(5)+facttest(4)+facttest(3)+facttest(2)+facttest(1)
print("first 5 factorial sum=",s)



factorila number no return value no argumnet
factorila number no return value with argumnet
factorila number return value with no argumnet

factorila number return value with  argumnet
def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
print("enter a number ")
res=fcattest(int(input()))
print("factorial=",res)