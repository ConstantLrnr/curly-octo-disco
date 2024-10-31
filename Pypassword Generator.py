letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
 
symbols = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/']
 
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
 
import random


choice_of_letters =[letters]
password = random.sample(letters,nr_letters) #sample unique letters

password_string1=""
for letters in password:
    password_string1 += letters #concatenate each letter
part1=(password_string1)

choice_of_numbers =[numbers]
password = random.sample(numbers,nr_numbers) #sample unique numbers

password_string2=""
for numbers in password:
    password_string2 += numbers #concatenate each number
part2=(password_string2)

choice_of_symbols =[symbols]
password = random.sample(symbols,nr_symbols) #sample unique symbols

password_string3=""
for symbols in password:
    password_string3 += symbols #concatenate each symbol
part3=(password_string3)

Generic_Password=(part1+part2+part3)

Generic_Password_List= list(part1+part2+part3) #converts string to a list
random.shuffle(Generic_Password_List) #shuffles the list
#shuffles list back to a string
shuffled_Generic_Password=""
for parts in Generic_Password_List:
    shuffled_Generic_Password += parts
Generated_Password=(shuffled_Generic_Password)    

print("Here is your new password: " + Generated_Password)
