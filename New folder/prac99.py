class Demo:
    c=0
    def __init__(self,a):
        Demo.c=a+2
        self.a=a
    def update(self,a):
        Demo.c= Demo.c+a
        self.a= self.a+a
    def show(self):
        print(self.a,Demo.c)
d= Demo(1)
d1=Demo(2)
d2=Demo(3)
d.show() # 1 5
d1.show() # 2 5
d2.show() # 3 5
d.update(3)
d1.update(5)
d2.update(7)
d2.c = 4
d.show() # 4 4
d1.show() # 6 4
d2.show() # 8 4