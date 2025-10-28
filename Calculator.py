import os
import Calculator_art #this gets the logo from the file called Calculator_art
print(Calculator_art.Calc)  #this prints the logo

def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1/n2

calculate = {
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
}


n1 = int(input("What is the first number?: "))
symbol = (input("Pick an operation (+ , - , * , /): "))
n2 = int(input("What is the next number? : "))

Answer = calculate.get(symbol) #In the dictionary calculate, look up the key that matches the value in symbol/ dictionary.get(key)


x = Answer(n1,n2) #this call it to get the answer
print(f"Your answer is: {x}")
cont = (input(f"type 'y' to continue with {x}, or type 'n' to start a new calculation: "))

if cont =='y':
    symbol = (input("Pick an operation (+ , - , * , /): "))
    n2 = int(input("What is the next number? : "))
    
    Answer = calculate.get(symbol)
    x2 = Answer(x,n2)
    print(f"Your answer is: {x2}")
    cont = (input(f"type 'y' to continue with {x}, or type 'n' to start a new calculation: "))
    
if cont == 'n':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Calculator_art.Calc)
    n1 = int(input("What is the first number?: "))
    symbol = (input("Pick an operation (+ , - , * , /): "))
    n2 = int(input("What is the next number? : "))