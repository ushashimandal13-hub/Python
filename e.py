class Student:
    def __init__(self):
    	self.name="Ushashi"
    def dispA(self):
    	print("Student's name- ", self.name)
class Marks(Student):
	def __init__(self):
		super().__init__()
		self.y = 20
	def dispB(self):
		print("Student's marks= " ,self.y)

ob=Marks()
ob.dispA()
ob.dispB()
