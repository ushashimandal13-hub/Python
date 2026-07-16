class Demo:
    c=0
    def __init__(self):
        Demo.c=1
        self.a=1
    def update(self,a):
        Demo.c= Demo.c+1
        self.a= self.a+a
    def show(self):
        print(self.a,Demo.c)
d= Demo()
d1=Demo()
d2=Demo()
d.show() # 1 1
d1.show() # 1 1
d2.show() # 1 1
d.update(3)
d1.update(5)
d2.update(7)
d.show() # 4 4
d1.show() # 6 4
d2.show() # 8 4