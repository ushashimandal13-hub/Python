print("Enter Three numbers: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())
if(n1> n2 and n1>n3):
    print("Largest number is: ", n1)
elif(n2>n3):
    print("Largest number is: ", n2)
else:
    print("Largest number is: ", n3)    