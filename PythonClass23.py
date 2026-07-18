acess modifier
__________
private    __
protected   _
public
           not avaliable python

______________

class A:
	def __init__(self):
		self.a=10 #public
		self.__b=20 #private
	def look(self):
		return self.__b
ob=A()
print(ob.a)
#print(ob.__b)# error
print(ob.look())





class A:
	def __init__(self):
		self.a=10 #public
		self.__b=20 #private
	def __look(self):  #private
		print("look function")
	def show(self): #public
		self.__look()
		print(self.__b)
ob=A()
print(ob.a)
#print(ob.__b)# error
#ob.look()  #error
ob.show()

Name Mangling
_______________
A private member starts with double underscore (__).

Python performs name mangling, changing __name to _ClassName__name.


class Student:
    def __init__(self):
        self.__mark = 90

s = Student()

print(s._Student__mark)




setter and getter 
_____________________
class Student:
	def __init__(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def disp(self):
		print("my name=",self.__name)
		print("my rollno=",self.__roll)
		print("my mark=",self.__mark)
	def update(self,n,r,mark):
		self.__name=n
		self.__roll=r
		self.__mark=mark
	def set__name(self,name):
		self.__name=name
	def set__roll(self,roll):
		self.__roll=roll
	def set__mark(self,mark):
		self.__mark=mark
	def get__name(self):
		return self.__name
	def get__roll(self):
		return self.__roll
	def get__mark(self):
		return self.__mark
s=Student("muna",1,90.50)
print(s.__dict__)
s.disp()
s.update("muna das",2,90)
s.disp()
s.set__name("muna kumar das")
print("my name=",s.get__name())
print("my rollno=",s.get__roll())
print("my mark=",s.get__mark())













class Student:
    def __init__(self, name, roll, mark):
        self.__name = name
        self.__roll = roll
        self.__mark = mark

    # Getter
    @property
    def name(self):
        return self.__name

    @property
    def roll(self):
        return self.__roll

    @property
    def mark(self):
        return self.__mark

    # Setter
    @name.setter
    def name(self, value):
        self.__name = value

    @roll.setter
    def roll(self, value):
        self.__roll = value

    @mark.setter
    def mark(self, value):
        self.__mark = value


# Object
s = Student("Muna", 1, 90)

print("Name :", s.name)
print("Roll :", s.roll)
print("Mark :", s.mark)

# Update values
s.name = "Muna Das"
s.roll = 2
s.mark = 95

print("\nAfter Update")

print("Name :", s.name)
print("Roll :", s.roll)
print("Mark :", s.mark)




Example 2: Validation using Setter

class Student:
    def __init__(self, mark):
        self.__mark = mark

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        if 0 <= value <= 100:
            self.__mark = value
        else:
            print("Invalid Marks")


s = Student(80)

print(s.mark)

s.mark = 95
print(s.mark)

s.mark = 150
print(s.mark)




Example 3: Read-Only Property


class Student:
    def __init__(self, roll):
        self.__roll = roll

    @property
    def roll(self):
        return self.__roll


s = Student(101)

print(s.roll)

# s.roll = 200   # Error




1. What is a property in Python?

A property is a special attribute controlled using the @property decorator that allows methods to be accessed like normal attributes.

2. Why use @property?
Encapsulation
Data validation
Cleaner syntax
Hides implementation details
3. Difference between getter/setter and property?
Getter/Setter Method	Property
Uses methods	Uses decorators
obj.getName()	obj.name
obj.setName()	obj.name = value
More verbose	Cleaner and recommended

static block in python
_______________________
class A:
	print("static block A")
print(A)
print(A)

o/p:
static block A
<class '__main__.A'>
<class '__main__.A'>


class A:
    x = 10
    y = 20
    print("Class body executing")
print(A.x)
print(A.y)








class A:
    print("Class body executed")

    def __init__(self):
        print("Constructor called")

a1 = A()
a2 = A()



o/p:
Class body executed
Constructor called
Constructor called






class A:
    print("Class Body (Static-like)")

    def __init__(self):
    	self.nonstatic()
    	print("constructor")
    def nonstatic(self):
    	print("non static block")


a1 = A()
a2 = A()


o/p:
Class Body (Static-like)
non static block
constructor
non static block
constructor






rectangle
___________


len bre private
constructor 
setter and getter 
area()
peri()