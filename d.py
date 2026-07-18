class A:
    def __init__(self):
    	self.x=10
    def dispA(self):
    	print(self.x)
class B(A):
	def __init__(self):
		super().__init__()
		self.y=20
	def dispB(self):
		print(self.y)

ob=B()
ob.dispA()
ob.dispB()
