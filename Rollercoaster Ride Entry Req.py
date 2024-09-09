height = int(input ("What is your height in CM? "))

if height >= 120:
   print("Welcome to the rollercoaster!") 
   Age= int(input("what is your age? "))
   if Age <= 12:
    print("You must pay $5 to ride")
   elif Age <=18:
    print("You must pay $7 to ride")
   else :
    print("You must pay $12 to ride")
else:
   print("Sorry, you will have to grow taller before you can ride!!")