print("Enter a number: ")
num = int(input())
if(num<=9):
    print("Num is single digit")
elif(num<=99):
    print("Num is double digit")
elif(num<=999):
    print("Num is triple digit")
else:
    print("Num is other digit")