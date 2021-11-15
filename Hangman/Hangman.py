import random
from hangman_word import word_list
from hangman_art import stages, logo

# Variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Game starts from here
exit = True
while exit: 
    print(logo)
    display = ['_'] * word_length
    print(*display)

    end_of_game = False
    while end_of_game == False:

        #Check guessed letter
        guess = input("Guess a letter: ").lower()
        if guess not in chosen_word:
            lives -= 1
            print("You guessed wrong word.")
        else:
            for x in range(word_length):
                letter = chosen_word[x]
                if letter == guess:
                    display[x] = letter 
        print(f"{' '.join(display)}")   #Join all the elements in the list and turn it into a String.
        print(stages[lives])
        
        if lives == 0:
            end_of_game = True
            print("The word was: " + chosen_word.upper())
            print("Game over")
        elif "_" not in display:
            end_of_game = True
            print("You win.")

    last = input("Do you want to play again? (y/n) ")
    if last == 'n':
        exit = False