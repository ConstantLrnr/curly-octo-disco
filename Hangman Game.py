import random

import hangman_art
print(hangman_art.logo)

from words_list import words
import hangman_stages

chosen_word = random.choice(words).lower() #converts chosen word to lower case
#print(chosen_word)
#this goes through the chosen word and places underscores
placeholder = " "
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(placeholder)


game_over = False
correct_letters = []


lives = 6 #start with 6 lives


while not game_over:
    
    valid_guess = False #defined 
    
    while not valid_guess: #this inner loop handles repeated guesses
        guess = input("Guess a letter : ").lower()
    #place_holder = "_ " * len(chosen_word)# list of underscores #this replaces each letter with
    #a "_ " and a space between each dash print(place_holder)
    
    #check if the guess has already been made
        if guess in correct_letters:
            print(f"You have already guessed this letter :{guess}")    
        else:
            valid_guess = True  #exit inner loop when a valid guess is made
    
    #update the display based on correct guesses
    display = ""  
    for letter in chosen_word:
        if letter == guess:
            display += letter #add the current letter to the display
            correct_letters.append(guess) #mark the letter as guessed  
        elif letter in correct_letters:
            display += letter  #if letter was guessed before, show it
        else: 
            display += "_ "  #if the letter does not match we will give an "_"
    print(display)   #show current state of the word     
            
    if guess not in chosen_word:
        lives -= 1
        print(f"This letter is not matching anything!!!! You lose a LIFE!: {guess}")
        print(hangman_stages.stages[6 - lives]) #display the hangman stage
        print(f"**************lives left: {lives}/6*************")
        #print (f"stages index: {6 - lives}")
        
            
        if lives == 0: #end games if no lives remain
            game_over = True 
            print(f"You Lose! The word was '{chosen_word}'.I cant believe you did not get this!!!!")
                  
    if "_" not in display: #check if the word is fully guessed
        game_over = True
        print("************You win!************")
