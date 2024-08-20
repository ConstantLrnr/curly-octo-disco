# welcome to the tip calculator
# what was the total bill?
# how much tip would you like to give? 10,12, or 15? 
# how many people to split the bill?
# Each person should pay:

(TB)= ("what was the total bill? ")
(Tip)= ("How much tip would you like to give? 10,12, or 15? ")
(Split)= ("how many people to split the bill? ")
(Pay)= ("Each person should pay:" )

print("Welcome to the Tip Calculator!") 
TB= float(input("What was the total Bill? ")) 
Tip= int(input("how much tip would you like to give? 10, 12, 15? "))
Split= int(input("How many people to split the bill? "))

Pay= TB * Tip/100 + 1 / Split

print(f"Each person should Pay: {Pay:.2f}")
