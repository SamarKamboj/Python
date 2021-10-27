import random
import hangman_word
import hangman_art

# Variables
art1 = hangman_art.logo
art2 = hangman_art.stages
wordList = hangman_word.word_list
chosen_word = random.choice(wordList)
word_length = len(chosen_word)
lives = 6

# Game starts from here


exit = True
while exit == True: 
    print(art1)
    display = []  # --> Empty List
    for x in range(word_length):
        display.append("_")  # Adding blanks in list 

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
        print(art2[lives])
        
        if lives == 0:
            end_of_game = True
            print("The word was: " + chosen_word.upper())
            print("Game over")
        elif "_" not in display:
            end_of_game = True
            print("You win.")

    last = int(input("Type 0 to Exit or Any number to Play Again.\n"))
    if last == 0:
        exit = False
