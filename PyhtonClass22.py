oops
____________________
#wap store one student name rollno and mark display it
name="muna"
r=1
mark=90.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)

o/p:
my name=muna
my rollno=1
my mark=90.50


#wap store two student name rollno and mark display it

name="muna"
r=1
mark=90.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)
name="kuna"
r=2
mark=80.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)


o/p:
my name=muna
my rollno=1
my mark=90.50
my name=kuna
my rollno=2
my mark=80.50


name="muna"
r=1
mark=90.50
name="kuna"
r=2
mark=80.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)

o/p:
my name=kuna
my rollno=2
my mark=80.50

here first  student data loss

if we store 2 student data  requried 2 name 2 rollno and 2 mark


name="muna"
r=1
mark=90.50
name1="kuna"
r1=2
mark1=80.50
print("my name=",name)
print("my rollno=",r)
print("my mark=",mark)
print("my name=",name1)
print("my rollno=",r1)
print("my mark=",mark1)


o/p:
my name=muna
my rollno=1
my mark=90.50
my name=kuna
my rollno=2
my mark=80.50


if we store 100 student data  requried 100 name 100 rollno and 100 mark
correct 
this type program is not good  solve these program using oops.

class
object
constructor
destructor
inheritance
polymorphism
abstrcation

Python Class and Object (Theory)
What is a Class?

A class is a blueprint or template used to create objects. It defines the data (attributes) and functions (methods) that an object will have.

Think of a class as the design of a house, while an object is the actual house built from that design.

how to define class
__________________

class classname:
	related data and method
	....
	.....
	constructor
	destructor
	method

A class generally contains:

Data (Attributes)
Constructor
Methods
Destructor (optional)


What is an Object?
________________________
An object is an instance of a class.

It is a real-world entity that contains its own data and can perform actions using methods.

Example:

Class → Student
Objects → Rahul, Priya, Amit

All are different students but belong to the same class
how to create object
_______________
classname(args)   # object creation    nameless object

objectrefernce=classname(args)



How to acess object data and method
____________________________________
objectrefernce.data
objectrefernce.method(args)



example
_______________
class Student:
	pass
s=Student()
print(s.__dict__)

o/p:
{}


class Student:
    pass
s=Student()
s.name="muna"
s.rollno=1
print(s.__dict__)

o/p:
{'name': 'muna', 'rollno': 1}



class Student:
    pass
s=Student()
s.name="muna"
s.rollno=1
print(s.__dict__)
s1=Student()
s1.name="kuna"
print(s1.__dict__)

o/p:
{'name': 'muna', 'rollno': 1}
{'name': 'kuna'}



class Student:
    college = "SOA University"   # Class Variable

s1 = Student()
s2 = Student()
print(s1.__dict__)
print(s2.__dict__)
print(s1.college)
print(s2.college)
print(Student.college)
print(Student.__dict__)


o/p:
{}
{}
SOA University
SOA University
SOA University
{'__module__': '__main__', '__firstlineno__': 1, 'college': 'SOA University', '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
[Finished in 92ms]











class Student:
    clg="iter"
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 

print(s.__dict__)  # { }
print(Student.__dict__)
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
print("clg name better way =",Student.clg)
#print("my name=",Student.name)  error name is part of object 


o/p:
{'name': 'muna', 'rollno': 1}
{'__module__': '__main__', 'clg': 'iter', '__init__': <function Student.__init__ at 0x000001B9ADB0D120>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}
my name= muna
my rollno= 1
clg name= iter
clg name better way = iter





class Student:
    clg="iter"  #class variable common for all object
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        self.name="muna" # instance variable  object data 
        self.rollno=1
s=Student() # object create  got where constrcutor 
print("my name=",s.name)
print("my rollno=",s.rollno)
print("clg name=",s.clg)
s1=Student()
print("my name=",s1.name)
print("my rollno=",s1.rollno)
print("clg name=",s1.clg)


o/p:
my name= muna
my rollno= 1
clg name= iter
my name= muna
my rollno= 1
clg name= iter

here all data same  
change all data difffernt input from keyboard 


class Student:
    clg="iter"  #class variable common for all object
    def __init__(self): # constructor but in java and c++ constructor same as classname
        print("enter name and roll number ")
        self.name=input() # instance variable  object data 
        self.rollno=int(input())
s=Student() # object create  got where constrcutor 
s1=Student()
print("clg name=",Student.clg)
print("my name=",s.name)
print("my rollno=",s.rollno)
print("my name=",s1.name)
print("my rollno=",s1.rollno)

o/p:
enter name and roll number
muna
1
enter name and roll number
kuna
2
clg name= iter
my name= muna
my rollno= 1
my name= kuna

class Student:
    clg="iter"  #class variable common for all object
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        print("enter name and roll number ")
        self.name=input() # instance variable  object data 
        self.rollno=int(input())
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)

s=Student() # object create  got where constrcutor 
s1=Student()
print("clg name=",Student.clg)
s.show()
s1.show()

o/p:
a das
1
enter name and roll number
b das
2
clg name= iter
my name= a das
my rollno= 1
my name= b das
my rollno= 2


class Student:
    def __init__(self):   # constructor   but in java and c++ constructor same as classname
        print("enter name and roll number ")
        self.name=input() # instance variable  object data 
        self.rollno=int(input())
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)
s=Student() # object create  got where constrcutor 
s1=Student()
s.show()
s1.show()


A constructor is a special method in a class that is automatically called when an object is created. It is mainly used to initialize (assign values to) the object's instance variables.

In Python, the constructor is written using the special method:

class ClassName:
    def __init__(self):
        # initialization code
__init__ → Constructor method.
self → Refers to the current object.
It is automatically called when an object is created.


Why Do We Need a Constructor?

Without a constructor:

We must assign values manually after creating the object.
More code is required.
Objects may remain uninitialized.

With a constructor:

Object is ready immediately after creation.
Saves time.
Makes code cleaner and easier to maintain.



Example Without Constructor
______________________

class Student:
    pass

s = Student()

s.name = "Rahul"
s.roll = 101

print(s.name)
print(s.roll)

Example With Constructor
______________________

class Student:

    def __init__(self):
        self.name = "Rahul"
        self.roll = 101

s = Student()

print(s.name)
print(s.roll)

usig parameter constructor
______________________________

class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)
s=Student("muna",1) # object create  go to  constrcutor 
s1=Student("kuna",2)
s.show()
s1.show()


o/p:
my name= muna
my rollno= 1
my name= kuna
my rollno= 2

parameter constructor with keyboard
______________________________________

class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(self):
        print("my name=",self.name)
        print("my rollno=",self.rollno)
print("enter student name and rollno")
n=input()
r=int(input())
s=Student(n,r)
s.show()























class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("my name=",self.name)
		print("my rollno=",self.roll)
		print("my mark=",self.mark)
s=Student("muna",1,90.50)
s1=Student("kuna",2,80.50)
s.show()
s1.show()

o/p:
enter student name and rollno
a das
3
my name= a das
my rollno= 3







class Student:
    def __init__(self,n,r):   #parameter constructor   but in java and c++ constructor same as classname
        self.name=n # instance variable or  object data 
        self.rollno=r
    def show(s):  #self postion write any name
        print("my name=",s.name)
        print("my rollno=",s.rollno)
print("enter student name and rollno")
n=input()
r=int(input())
s=Student(n,r)
s.show()





o/p:
enter student name and rollno
a das
3
my name= a das
my rollno= 3





class Rectangle:
    def __init__(self,L,B):  
        self.L=L
        self.B=B
    def show(self):  
        print("length=",self.L)
        print("breadth=",self.B)
    def area(self):
        return self.L*self.B 
    def peri(self):
        print("perimeter=",2*(self.L+self.B))
print("enter rectangle length and breadth ")
Len=float(input())
Bre=float(input())
r=Rectangle(Len,Bre)
r.show()
print("area of rectangle=",r.area())
r.peri()



o/p:
C:\Users\LENOVO\OneDrive\Desktop\python9pm>py 1.py
enter rectangle length and breadth
5
7
length= 5.0
breadth= 7.0
area of rectangle= 35.0
perimeter= 24.0


destructor
____________
A destructor is a special method in Python that is automatically called when an object is about to be destroyed (deleted). It is mainly used to release resources such as files, database connections, sockets, or other external resources.


class ClassName:
    def __del__(self):
        # Cleanup code



| Constructor                                    | Destructor                         |
| ---------------------------------------------- | ---------------------------------- |
| `__init__()`                                   | `__del__()`                        |
| Called automatically when an object is created | Called when an object is destroyed |
| Initializes object data                        | Cleans up resources                |
| Executed first                                 | Executed last                      |


object life cycle
_________________
Object Created
      │
      ▼
__init__() Called
      │
      ▼
Object Used
      │
      ▼
Object Destroyed
      │
      ▼
__del__() Called



constructor
________________
A constructor is a special method in Python used to initialize objects of a class. The most commonly used constructor method is __init__(). 
Syntax of Constructor

class ClassName:
    def __init__(self):    #constructor
         # initialization code


Key Points:
__init__() is automatically called when a new object is created.

It is used to assign values to object properties or do any setup.

self refers to the current object.




class Test:
    def __init__(self):
        print("constructor")
t=Test()
t1=Test()
t2=Test()

o/p:
constructor
constructor
constructor



Example 1: Basic Constructor

class Student:
    def __init__(self):   # constructor
        print("Constructor is called!")

s1 = Student()  # object creation

o/p:
constructor is called


note : every class by default constructor avaliable
class Demo:
    pass

d = Demo()
print(d.__init__)         # Show the default constructor
print(type(d.__init__))   # Show type

o/p:
<method-wrapper '__init__' of Demo object at 0x0000022AF8886690>
<class 'method-wrapper'>


class MyClass:
    pass

help(MyClass)


o/p:
Help on class MyClass in module __main__:

class MyClass(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object


class MyClass:
    pass

print(MyClass.__init__)           # Show the constructor function
print(MyClass.__init__ == object.__init__)  # Check if it's inherited from object

o/p:
<slot wrapper '__init__' of 'object' objects>
True





class Test:
    def __init__(self):
        self.x=0
        self.y=0
t=Test()
t1=Test()
t2=Test()
t.x=10
t.y=20
print(t.x)
print(t.y)
t1.x=30
t1.y=40
print(t1.x)
print(t1.y)

print(t2.x)
print(t2.y)

print(t.__dict__)
print(t1.__dict__)
print(t2.__dict__)


o/p:
10
20
30
40
0
0
{'x': 10, 'y': 20}
{'x': 30, 'y': 40}
{'x': 0, 'y': 0}

class Test:
    def __init__(self):
        self.x=0
        self.y=0
t=Test()
t1=Test()
t2=Test()
print(t.__dict__)
print(t1.__dict__)
print(t2.__dict__)

o/p:
{'x': 0, 'y': 0}
{'x': 0, 'y': 0}
{'x': 0, 'y': 0}



parameter constructor
___________________________
class Test:
    def __init__(self,a,b):
        print("parameter constructor ",a,b)
t=Test(10,20)
t1=Test(30,40)
#t2=Test()  error no argument


o/p:
parameter constructor 10 20
parameter constructor 30 40




class Test:
    def __init__(self,x,y):
        self.x=x
        self.y=y
t=Test(10,20)
t1=Test(30,40)
t2=Test(50,60)
print(t.__dict__)
print(t1.__dict__)
print(t2.__dict__)


o/p:

{'x': 10, 'y': 20}
{'x': 30, 'y':40}
{'x': 50, 'y': 60}


constructor overloading not allow in python
__________________________________________

we can write more constructor inside class last constructor is final




class Test:
    
    def __init__(self,x):
        print("parameter constructor")
    def __init__(self):
        print("basic constructor")
t=Test()
o/p:
basic constructor


class Test:  
    def __init__(self):
        print("basic constructor")
    def __init__(self,x):
        print("parameter constructor")
t=Test(10)

o/p:
parameter constructor

note :
if we are write more than constructor last one final.


class Test:  
    def __init__(self):
        print("basic constructor")
    def __init__(self,x):
        print("parameter constructor")
t=Test(10)
t1=Test()    # error

o/p:
parameter constructor
Traceback (most recent call last):
  File "C:\Users\LENOVO\OneDrive\Desktop\python9pm\lsw.py", line 7, in <module>
    t1=Test()
       ^^^^^^
TypeError: Test.__init__() missing 1 required positional argument: 'x'

 constructor  default parameter
 ________________________________

class Test:  
    def __init__(self,x=0):
        print("default  constructor ",x)
t=Test(10)
t1=Test()

o/p:
default  constructor  10
default  constructor  0




Example 3: Default Values in Constructor
class Student:
    def __init__(self, name="Unknown"):
        self.name = name
    def show(self):
        print("Name:", self.name)
s1 = Student()
s2 = Student("Priya")
s1.show()
s2.show()

o/p:
Name: Unknown
Name: Priya


destructor
__________________
A destructor is a special method in Python called when an object is about to be destroyed, i.e., when it goes out of scope or is explicitly deleted using del.

🔹 Syntax of Destructor
def __del__(self):
    # cleanup code


🔍 Key Points:
Destructor method name is __del__().

It is automatically called when the object is garbage collected.

Mainly used for cleanup operations like closing files or releasing resources.



class Test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
t1=Test()
t2=Test()
t3=Test()


constructor
constructor
constructor
destructor
destructor
destructor



https://chatgpt.com/share/68765041-edfc-8008-a177-bf724e2b2213


class Test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
t1=Test()
t1=None
t2=Test()
t3=Test()

o/P
constructor
destructor
constructor
constructor
destructor
destructor












class Test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
t1=Test()
del t1
t2=Test()
t3=Test()

o/P
constructor
destructor
constructor
constructor
destructor
destructor


class Test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
t1=Test()
t2=Test()
t1=t2
t3=Test()

o/p:
constructor
constructor
destructor
constructor
destructor
destructor



class Test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
def show():
    print("show function start")
    t2=Test()
    print("show function end")
t1=Test()
show()
t3=Test()

o/p:
constructor
show function start
constructor
show function end
destructor
constructor
destructor
destructor





class Test:
    def __init__(self,x):
        self.x=x
        print("constructor")
    def __del__(self):
        print("destructor ",self.x)
def show():
    print("show function start")
    t2=Test(20)
    print("show function end")
t1=Test(10)
show()
t3=Test(30)

o/P:
constructor
show function start
constructor
show function end
destructor  20
constructor
destructor  10
destructor  30




Python uses automatic garbage collection to free up memory from unused objects.
The gc module lets you:

Manually trigger garbage collection.

Enable or disable the garbage collector.

Track unreachable objects.




import gc

class Test:
    def __init__(self, x):
        self.x = x
        print("constructor")

    def __del__(self):
        print("destructor", self.x)

def show():
    print("show function start")
    t2 = Test(20)
    print("show function end")
    # Force garbage collection inside show()
    gc.collect()
    print("bye")
t1 = Test(10)
show()
t3 = Test(30)

# Force garbage collection at the end
gc.collect()



o/p:
constructor
show function start
constructor
show function end
bye
destructor 20
constructor
destructor 10
destructor 3


class Student:
    def set(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m
    def show(self):
        print("my name=",self.name)
        print("rollno=",self.roll)
        print("mark=",self.mark)
s=Student()
s.set("muna",1,90.50)
s.show()

using method to initlize  data   call the method



better we choose constructor for initlize datamemeber or propertits
method use explore  the data



class Student:
    def __init__(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m
    def show(self):
        print("my name=",self.name)
        print("rollno=",self.roll)
        print("mark=",self.mark)
s=Student("muna",1,90.50)
s.show()





class Student:
    def __init__(self, name, roll):
        # Constructor
        self.name = name
        self.roll = roll
        print("Constructor called")

    def display(self):
        # Method
        print("Name:", self.name)
        print("Roll No:", self.roll)

# Creating object – constructor is called automatically
s1 = Student("Alice", 101)

# Calling method explicitly
s1.display()

| Feature           | **Constructor**                                          | **Method**                                    |
| ----------------- | -------------------------------------------------------- | --------------------------------------------- |
| **Purpose**       | Used to **initialize** an object when it's created       | Used to **perform operations** on object data |
| **Name**          | Always `__init__()`                                      | Any valid function name                       |
| **Called when?**  | Automatically called **once** when an object is created  | Called **manually** using the object          |
| **Return type**   | Must **not return anything explicitly** (returns `None`) | Can return any value                          |
| **Defined using** | `def __init__(self):`                                    | `def method_name(self):`                      |
| **Usage**         | Sets initial values of object attributes                 | Defines behaviors or actions                  |
| **Call syntax**   | Automatically called: `obj = ClassName()`                | Called like: `obj.method_name()`              |


Constructor = Initialization

Method = Behavior/Action

You usually define a constructor once per class, but you can define many methods.









different types of variable
________________________________

(1)local 
(2)global
(3)instance
(4)class

local variable
___________________
class Demo:
    def __init__(self):
        a=10
        print("local variable=",a)
    def show(self,b):
        e=40
        print("local or formal parameter =",b)
def disp():
    c=30
    print("local varaiable =",c)
ob=Demo()
disp()
ob.show(50)
#print(a) error local varaiable outside the block
#print(b)
#print(c)

global variable
__________________
a=10
class Demo:
    def __init__(self):
        print("global  variable=",a)
    def show(self,b):
        global a
        print("global variable =",a)
        a=30
def disp():
    print("global varaiable =",a)
ob=Demo()
disp()

ob.show(50)
print(a) 
a=50
print(a)


o/p:
global  variable= 10
global varaiable = 10
global variable = 10
30
50




a=10 # global variable  
class Demo:
    def __init__(self):
        b=20  #local variable
    def show(self,b):
        c=30   #local variable
ob=Demo()
print(ob.__dict__)
o/p:
{  }



instance variable 
_________________
a=10 # global variable  
class Demo:
    def __init__(self):
        self.b=20  #instance variable
    def show(self):
        e=50
        self.c=30   #instance variable
ob=Demo()
print(ob.__dict__)
ob.show()
print(ob.__dict__)
ob.d=40
print(ob.__dict__)


o/p:
{'b': 20}
{'b': 20, 'c': 30}
{'b': 20, 'c': 30, 'd': 40}

we can create instance variable any location 



per object per instance variable
______________________________
a=10 # global variable  
class Demo:
    def __init__(self):
        self.b=20  #instance variable
    def show(self):
        self.c=30   #instance variable
ob=Demo()
print(ob.__dict__)
ob.show()
print(ob.__dict__)
ob.d=40
print(ob.__dict__)
ob1=Demo()
print(ob1.__dict__)
ob1.x=50
print(ob1.__dict__)

o/p:
{'b': 20}
{'b': 20, 'c': 30}
{'b': 20, 'c': 30, 'd': 40}
{'b': 20}
{'b': 20, 'x': 50}


class variable:



class Demo:
    a=10   #class variable
    def __init__(self):
        self.b=20  #instance variable
        
    def show(self):
        self.c=30   #instance variable
ob=Demo()
print(ob.__dict__)
ob.show()
print(ob.__dict__)
print(Demo.__dict__)

o/P:
{'b': 20}
{'b': 20, 'c': 30}
{'__module__': '__main__', 'a': 10, '__init__': <function Demo.__init__ at 0x0000026D64CAD300>, 'show': <function Demo.show at 0x0000026D64CAD120>, '__dict__': <attribute '__dict__' of 'Demo' objects>, '__weakref__': <attribute '__weakref__' of 'Demo' objects>, '__doc__': None}









class Demo:
    a=10   #class variable
    def __init__(self):
        self.b=20  #instance variable
        g=90 #local variable
    def show(self):
        self.c=30   #instance variable
ob=Demo()
#print(ob.__dict__)  #{ 'b': 20}
ob.show()
#print(ob.__dict__)  #('b':20 ,'c':30')
#print(Demo.__dict__) #{extra  ,'a':10}
print(ob.b,ob.c,ob.a,Demo.a)
#print(g)  local variabl   not acess outside


o/p:
20 30 10 10

 equvalient java code 
 __________________________
class Demo {
    static int a = 10; // class variable
    int b;             // instance variable
    int c;             // instance variable (assigned in show)

    Demo() {
        b = 20;
        int g = 90; // local variable, only accessible in constructor
    }

    void show() {
        c = 30; // instance variable
    }

    public static void main(String[] args) {
        Demo ob = new Demo();
        ob.show();

        System.out.println(ob.b + " " + ob.c + " " + ob.a + " " + Demo.a);
        // or optionally with labels:
        // System.out.println("b=" + ob.b + " c=" + ob.c + " a=" + ob.a + " Demo.a=" + Demo.a);
    }
}

class Demo:
    a=10   #class variable
    def __init__(self):
        self.b=20  #instance variable
        g=90 #local variable
    def show(self):
        self.c=30   #instance variable
ob=Demo()
#print(ob.__dict__)  #{ 'b': 20}
ob.show()
#print(ob.__dict__)  #('b':20 ,'c':30')
#print(Demo.__dict__) #{extra  ,'a':10}
print(ob.b,ob.c,ob.a,Demo.a)  #20 30 10 10
print(ob.__dict__) #('b':20 ,'c':30')
ob.a=50
print(ob.__dict__) #('b':20 ,'c':30','a:50)
print(ob.a,Demo.a) #50 10
Demo.a=70
print(ob.a,Demo.a) #50 10

o/p:
20 30 10 10
{'b': 20, 'c': 30}
{'b': 20, 'c': 30, 'a': 50}
50 10
50 70




class Demo:
    a = 10
    def __init__(self):
        self.b = 20  # instance variable

    def show(self):
        self.c = 30  # instance variable

ob = Demo()
ob.show()
ob.d = 40  # dynamically added attribute
print(ob.b, ob.c, ob.d)

o/p:
20 30 40 

❗ Key Points:
b is initialized in __init__

c is initialized in show()

d is dynamically added to the object after creation — this is possible in Python, but not allowed in Java (Java doesn't allow adding new attributes dynamically to an object after it's created).

class Demo {
    int b; // instance variable
    int c; // instance variable
    int d; // extra variable manually added in Java

    Demo() {
        b = 20;
    }

    void show() {
        c = 30;
    }

    public static void main(String[] args) {
        Demo ob = new Demo();
        ob.show();
        ob.d = 40;  // in Java, you must define this field in the class

        System.out.println(ob.b + " " + ob.c + " " + ob.d);
    }
}



differnence between instance variable and class variable
__________________________________________________
class Demo:
    a=10 
    def __init__(self):
        self.b=20  #instance variable
ob1=Demo()
ob2=Demo()
print(ob1.a,ob1.b) # 10 20
print(ob2.a,ob2.b) # 10 20
ob1.b=30
ob2.b=40
Demo.a=50
print(ob1.a,ob1.b) # 50 30
print(ob2.a,ob2.b) # 50 40



o/p:
10 20
10 20
50 30
50 40



class Demo:
    a=10 
    def __init__(self):
        self.b=20  #instance variable
ob1=Demo()
ob2=Demo()
print(ob1.a,ob1.b) # 10 20
print(ob2.a,ob2.b) # 10 20
ob1.a=30
ob2.b=40
Demo.a=50
print(ob1.a,ob1.b) # 30 20
print(ob2.a,ob2.b) #50 40

o/p:
10 20
10 20
30 20
50 40


# count no of object 

class Demo:
    c=0# class variable
    def __init__(self):
        Demo.c=Demo.c+1
ob1=Demo()
ob2=Demo()
ob3=Demo()
L=[Demo(),Demo(),Demo()]
print("no of object=",Demo.c)


o/P;
no of object=6



class Demo:
    c=0# class variable
    def __init__(self):
        Demo.c=1
        self.a=1
    def update(self):
        Demo.c=Demo.c+1
        self.a=self.a+1
    def show(self):
        print(self.a,Demo.c)
d=Demo()
d1=Demo()
d2=Demo()
d.update()
d1.update()
d2.update()
d.show()  #  
d1.show() #
d2.show() #


C:\Users\LENOVO\OneDrive\Desktop\pythonbiki>py p.py
2 4
2 4
2 4



class Demo:
    c=0# class variable
    def __init__(self):
        Demo.c=1
        self.a=1
    def update(self,a):
        Demo.c=Demo.c+1
        self.a=self.a+a
    def show(self):
        print(self.a,Demo.c)
d=Demo()
d1=Demo()
d2=Demo()
d.show()  #        1  1
d1.show() #        1  1
d2.show() #        1  1
d.update(3)        
d1.update(5)
d2.update(7)
d.show()  #    4   4            
d1.show() #    6   4  
d2.show() #     8  4


o/p:
1 1
1 1
1 1
4 4
6 4
8 4


class Demo:
    c=0# class variable
    def __init__(self,a):
        Demo.c=a+2
        self.a=a
    def update(self,a):
        Demo.c=Demo.c+a
        self.a=self.a+a
    def show(self):
        print(self.a,Demo.c)
d=Demo(1)
d1=Demo(2)
d2=Demo(3)
d.show()   # 1 5
d1.show()  # 2 5
d2.show()  # 3 5
d.update(3)        
d1.update(5)
d2.update(7)
d2.c=4
d.show()    #   4 20       
d1.show()   #  7  20
d2.show()   #  10 20


o/p:
1 5
2 5
3 5
4 20
7 20



https://chatgpt.com/share/6878f21c-f254-8008-8b72-d9730f613602




















method  in oops 
_____________________
instance method 
static method 
class maethod 



class Demo:
    #instance method call by object
    def show(self):
        print("hi")
d=Demo()# object create
d.show() #object refrence (d) call 
#Demo.show()  #not call by class




class Demo:
    #staticmethod  it call by classname  
    @staticmethod
    def show():
        print("hi")
Demo.show() #it call by classname
d=Demo()
d.show()



class Demo:
    #classmethod  it call by classname  but  it call  by object
    @classmethod
    def show(cls):
        print("hi")
Demo.show() #it call by classname  better
d=Demo()
d.show() # it call by object





class Demo:
    def show(self):
        print("instance show method")
    @classmethod
    def look(cls):
        print("class look method")
    @staticmethod
    def disp():
        print("disp static method")
d=Demo()
Demo().show() # by object call
d.show()  # it call by object  refernce 
d.look()
d.disp()
#Demo.show()  error
Demo.look()
Demo.disp()

constructor 
_________________
__init__   constructor special method 



class Rectangle:
    def __init__(self):   #constrcutor
        self.length=5
        self.breadth=7
    def show(self):
        print("rectangle lenegth=",self.length)
        print("rectangle breadth=",self.breadth)
    def area(self):
        print("area of rectangle=",self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())




class Rectangle:
    def __init__(self):   #constrcutor
        self.length=5
        self.breadth=7
    def show(self):
        print("rectangle lenegth=",self.length)
        print("rectangle breadth=",self.breadth)
    def area(self):
        print("area of rectangle=",self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())
r1=Rectangle()
r1.show()
r1.area()
print("perimeter of rectangle=",r1.perimeter())




class Rectangle:
    def __init__(self):   #constrcutor
        self.length=5
        self.breadth=7
    def show(self):
        print("rectangle lenegth=",self.length)
        print("rectangle breadth=",self.breadth)
    def area(self):
        print("area of rectangle=",self.length*self.breadth)
    def perimeter(self):
        return 2*(self.length+self.breadth)
r=Rectangle()
r.show()
r.area()
print("perimeter of rectangle=",r.perimeter())
r1=Rectangle()
r1.show()
r1.area()
print("perimeter of rectangle=",r1.perimeter())