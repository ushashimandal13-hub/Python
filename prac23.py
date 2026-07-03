def simcalc():
    print("Enter the principal amount: ")
    principal = float(input())
    print("Enter the rate of interest: ")
    rate = float(input())
    print("Enter the time: ")
    time = float(input())
    simple_interest = (principal * rate * time) / 100
    print("The simple interest is:", simple_interest)
simcalc()