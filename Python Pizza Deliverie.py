print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? Small, Medium, Large: " )
pepperoni = input("Do you want pepperonni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")         
Add_to_bill = 0

Small = 15
Medium = 20
Large = 25

if size == "Small":
    print(f"Small size pizza costs $ {Small}")
    Add_to_bill = 15
elif size == "Medium":
    print(f"Medium size pizza costs $ {Medium}")
    Add_to_bill = 20
elif size == "Large":
    print(f"Large size pizza costs $ {Large}")
    Add_to_bill = 25
else:
    print("You typed the wrong Inputs, (check CAPS)")

if pepperoni == "Y":
    if size == "Small": 
        Add_to_bill += 2
        Cost = 2
        print(f"Additional cost for Pepperoni is ${Cost}")
    if size == "Medium": 
        Add_to_bill += 3
        Cost = 3
        print(f"Additional cost for Pepperoni is ${Cost}")
    if size == "Large": 
        Add_to_bill += 3
        Cost = 3
        print(f"Additional cost for Pepperoni is ${Cost}")
    if extra_cheese == "Y":
        Add_to_bill += 1
        Cost = 1
        print(f"Additional cost for extra_cheese is ${Cost}")
        print(f"Your total is $ {Add_to_bill}")
else:
    print(f"Your total is $ {Add_to_bill}")
