class rectangle:
    def __init__(self,L,B):
        self.L=L
        self.B=B
    def show(self):
        print("Length= ",self.L)
        print("Breadth= ",self.B)
    def area(self):
        return self.L*self.B
    def perimeter(self):
        print("perimeter of rectangle= ", 2*(self.L+self.B))
print("Enter length and breadth of rectangle ")
L= int(input())
B= int(input())
r=rectangle(L,B)
r.show()
print("area of rectangle= ", r.area())
print("perimeter of the rectangle=" ,r.perimeter())