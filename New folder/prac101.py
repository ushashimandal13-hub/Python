class student:
    def __init__(self,n,r,m):
        self.__name=n
        self.__roll=r
        self.__mark=m
    @property
    def name(self):
        return self.__name
    
    @property
    def roll(self):
        return self.__roll
    
    @property
    def mark(self):
        return self.__mark
    
    @name.setter
    def name(self, value):
        self.__name = value

    @roll.setter
    def roll(self,value):
        self.__roll= value

    @mark.setter
    def mark(self, value):
        self.__mark = value

s= student("Tinny" , 24 , 9.1)
print("Name: ", s.name)
print("Roll no. = ",s.roll)
print("Mark= ",s.mark)
s.name = "Tinny Mandal"
s.roll = 25
s.mark = 9.5
print("After update")

print("Name: ",s.name)
print("Roll no. = ",s.roll)
print("Mark= ",s.mark)