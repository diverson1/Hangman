import random
import string
from words import word_list
from hangman_visuals import hangman_visuals as hv

def hangman():
    word = random.choice(word_list).upper()
    while not word.isalpha():
            word = random.choice(word_list).upper()

    letters_in_word = set(word) #Unique letters found in the word
    letters_guessed = set() #List of letters guessed
    alphabet = set(string.ascii_uppercase)
    
    lives_left = 7
    print('You have', lives_left, 'lives')
    while len(letters_in_word) != 0 and lives_left != 0:
        print('Letters you have guessed: ' , ' '. join(letters_guessed))
        word_display = []
        for letter in word:
            if letter in letters_guessed:
                word_display.append(letter)
                
            else:
                word_display.append('-')
        print('Current word is' , ' '.join(word_display))
        
        
        #user input
        print(' ')
        user_input = input('Guess a letter: ').upper()
        print(' ')

        if user_input in alphabet - letters_guessed:
            letters_guessed.add(user_input)
            if user_input in letters_in_word:
                letters_in_word.remove(user_input)
                print(hv[lives_left])
            else:
                lives_left -= 1
                print(hv[lives_left])
        elif user_input in letters_guessed:
            print('You already guessed that letter. Try again')
        else:
            print('Not an acceptable letter')
    if lives_left == 0:
        print('You lost, the word was', word)
    else:
        print('Nice job! The word was', word)

       
        
hangman()
