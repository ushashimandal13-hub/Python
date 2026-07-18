class student:
    def __init__(self,n,r,m):
        self.__name=n
        self.__roll=r
        self.__mark=m
    def disp(self):
        print("my name= ", self.__name)
        print("my roll no.= ",self.__roll)
        print("my mark= ",self.__mark)
    def update(self,n,r,mark):
        self.__name = n
        self.__roll=r
        self.__mark=mark
    def set__name(self,name):
        
        def set__roll(self,roll):
