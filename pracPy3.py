print("Enter a number")
no = int(input())
#convert +ve to -ve
if(no<0):
    no= -no
    print("negetive number", -no)
#check digits
elif no<10:
    print("Number is single digit")
elif no<100:
    print("Number is double digit")
else:
	print("od")
