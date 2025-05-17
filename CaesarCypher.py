import CaesarCypher_Art
print(CaesarCypher_Art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar(encode_or_decode,original_text, shift_amount): #combine the above functions into 1 new function
    grp_of_letters = 0
    new_WORD = "" #this holds the results
    
    while grp_of_letters < (len(original_text)):
        letters = original_text[grp_of_letters] #this shows the letter your at current time
                
        if letters in alphabet:
            origtextPos = alphabet.index(letters) #ths gives the position of the of origltr
            if encode_or_decode == 'encode':    
                new_letterno = origtextPos + shift_amount #ths adds the shift amt to the old position amt
            elif encode_or_decode == 'decode':
                new_letterno = origtextPos - shift_amount #ths subtracts the shift amt to the old position amt
            new_letterno %= len(alphabet) # keeps shift position within 0-25 (alphabet position)
            new_letter = alphabet[new_letterno] #alphabet is a list not a function so brackets should be used   
            new_WORD += new_letter # takes the current value of new_WORD and adds the new letter onto the end
        else:
            new_WORD += letters #just add it unchanged (ie: spaces and special characters)        
        grp_of_letters += 1  
        
    print(f"Here's the {encode_or_decode}d results: {new_WORD}")   

    Answer= input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if Answer == 'yes':
        encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        original_text = input("Type your message:\n")
        shift_amount = int(input("Type the shift number:\n"))
        caesar(encode_or_decode,original_text, shift_amount)
    if Answer == 'no':
        print('Goodbye!')

first_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
first_text = input("Type your message:\n")
first_shift = int(input("Type the shift number:\n"))        

caesar(first_direction,first_text, first_shift)