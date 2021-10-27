import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
infinite = 0
while infinite == 0:
    userInput = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
    rpsList = [rock, paper, scissor]

    userArt = rpsList[userInput]
    print(userArt)

    comprps = random.randint(0,2)
    computerArt = rpsList[comprps]
    for x in range(3):
        if x == comprps:
            print(f"Computer Chose: {computerArt}")


    if userInput > comprps:
        if userInput == 2 and comprps == 0:
            print("You loose!")
        else:
            print("You win!")

    elif userInput < comprps:
        if userInput == 0 and comprps == 2:
            print("You win!")
        else:
            print("You loose!")
    
    else:
        print("Draw!")
