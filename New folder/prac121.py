menu={"Pizza":300,
      "Fries":160.67,
      "Kabab":290,
      "Burger":150,
      "Chowmin":80,
      "Lemonade":40}
cart=[]
total=0
print("----MENU----")
for key,value in menu.items():
    print(f"{key:10}: Rs.{value}") 
print("------------")
while True:
    food=input("Select an item(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: ${total:2f}")