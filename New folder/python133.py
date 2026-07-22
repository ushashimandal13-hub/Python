try:
    num = int(input("Enter a number: "))
    print(num/0)
except ZeroDivisionError:
    print("You can't divided by zero Idiot!")
except ValueError:
    print("Please enter numbers")
except Exception:
    print("Somerhing went wrong!")
finally:
    print("Do some cleanup")


