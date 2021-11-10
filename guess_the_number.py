import random

logo = '''
 _______           _______  _______  _______   _________          _______    _                 _______  ______   _______  _______ 
(  ____ \|\     /|(  ____ \(  ____ \(  ____ \  \__   __/|\     /|(  ____ \  ( (    /||\     /|(       )(  ___ \ (  ____ \(  ____ )
| (    \/| )   ( || (    \/| (    \/| (    \/     ) (   | )   ( || (    \/  |  \  ( || )   ( || () () || (   ) )| (    \/| (    )|
| |      | |   | || (__    | (_____ | (_____      | |   | (___) || (__      |   \ | || |   | || || || || (__/ / | (__    | (____)|
| | ____ | |   | ||  __)   (_____  )(_____  )     | |   |  ___  ||  __)     | (\ \) || |   | || |(_)| ||  __ (  |  __)   |     __)
| | \_  )| |   | || (            ) |      ) |     | |   | (   ) || (        | | \   || |   | || |   | || (  \ \ | (      | (\ (   
| (___) || (___) || (____/\/\____) |/\____) |     | |   | )   ( || (____/\  | )  \  || (___) || )   ( || )___) )| (____/\| ) \ \__
(_______)(_______)(_______/\_______)\_______)     )_(   |/     \|(_______/  |/    )_)(_______)|/     \||/ \___/ (_______/|/   \__/
                                          
'''
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
randomNum = random.randint(1, 100)
print(randomNum)
difficultyLevel = input("Choose a difficulty. Type 'easy' or 'hard':\n")
if difficultyLevel == "easy":
    lives = 10
elif difficultyLevel == 'hard':
    lives = 5

end = True
while end:
    if lives == 0:
        print("Your attempts have been exhausted.")
        print(f"The number was {randomNum}. You loose.")
        end = False
    else:
        print(f"You have {lives} attempts remaining to guess a number.")
        userNum = int(input("Make a guess: "))
        if userNum != randomNum:
            lives -= 1
            if lives > 0:
                if userNum < randomNum:
                    print("Too low.")
                elif userNum > randomNum:
                    print("Too high.")
                print("Guess again.")
        elif userNum == randomNum:
            print(f"{userNum} Yes, You have successfully guessed the number. Well done!")
            end = False