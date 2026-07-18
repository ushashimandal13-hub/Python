weight = float(input("Enter your weight= "))
unit = input("Kilograms or pounds?(K or L): ")
if unit == "K":
    weight = weight*2.205
    unit = "Lbs"
    print(f"Your weight is: {round(weight)} {unit}")
elif unit == "L":
    weight = weight/2.205
    print(f"Your weight is: {round(weight)} {unit}")
else:
    print(f"{unit} was not valid")
