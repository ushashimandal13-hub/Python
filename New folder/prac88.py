class Test:
    def __init__(self,c):# c is local or formal variable
       a=10
       self.b=20
    def show(self):
        print(self.b)
        print(a)

        print(c)
t = Test(5)
print(t.b)
t.c=40
print(t.__dict__)
t1 = Test(8)
print(t1.__dict__)
#print(t.a) >>error
#print(t.c) >>error