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

rps = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))
rpsList = [rock, paper, scissor]
result = ["You win!", "You loose!", "Draw!"]

user = rpsList[rps]
print(user)

comprps = rpsList[random.randint(0,2)]
if (comprps == rock):
  print("Computer Chose: Rock")
elif (comprps == paper):
  print("Computer Chose: Paper")
elif (comprps == scissor):
  print("Computer Chose: Scissor")
print(comprps)

# Rock
if (user == rock) and (comprps == scissor):
  print(result[0])
elif (user == rock) and (comprps == paper):
  print(result[1])
elif (user == rock) and (comprps == rock):
  print(result[2])

# Paper
elif (user == paper) and (comprps == rock):
  print(result[0])
elif (user == paper) and (comprps == scissor):
  print(result[1])
elif (user == paper) and (comprps == paper):
  print(result[2])

# Scissor
elif (user == scissor) and (comprps == paper):
  print(result[0])
elif (user == scissor) and (comprps == rock):
  print(result[1])
elif (user == scissor) and (comprps == scissor):
  print(result[2])