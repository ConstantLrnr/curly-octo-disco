print("lets play Rock, Paper, Scissors with the computer!")
Your_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))

# Rock = 0
# Paper = 1
# Scissors =2

if Your_Choice >2:
    print("You typed an invalid # and You loose!")
   
    
if Your_Choice == 0:
    print("You Chose Rock")
    print(r"""
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
if Your_Choice == 1:
    print("You Chose Paper")
    print(r"""
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

if Your_Choice == 2:
    print("You Chose Scissors")
    print(r"""
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")



import random

Selection = [0, 1, 2]
Computer_Choice = random.randint(0, 2)
print(Selection[Computer_Choice])

if Computer_Choice == 0:
    print("Computer Chose Rock")
    print(r"""
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    
if Computer_Choice == 1:
    print("Computer Chose Paper")
    print(r"""
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

if Computer_Choice == 2:
    print("Computer Chose Scissors")
    print(r"""
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")
    
    

if Your_Choice == 0 and Computer_Choice == 2:
    print("You Win!")
elif Your_Choice == 2 and Computer_Choice == 1:
    print("You Win!")
elif Your_Choice == 1 and Computer_Choice == 0:
    print("You Win!")
elif Your_Choice == 0 and Computer_Choice == 1:
    print("You Lose!")
elif Your_Choice == 2 and Computer_Choice == 0:
    print("You Lose!")
elif Your_Choice == 1 and Computer_Choice == 2:
    print("You Lose!")     
elif Your_Choice == Computer_Choice:
    print ("Its a draw! chose again!")  
    