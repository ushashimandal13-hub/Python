print("Enter first number: ")
no1=int(input())
print("Enter second number: ")
no2=int(input())
print("Enter your choice \n1.Addition\n2.Substraction\n3.Multiplication")
int ch = int(input())
if ch==1:
	print("Addition", no1+no2)
elif ch==2:
	print("Substartion", no1+no2)
elif ch==3:
	print("Multiplication", no1*no2)
else:
	print("Invalid choice")
