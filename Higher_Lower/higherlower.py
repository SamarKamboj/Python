from random import randint
from game_data import data
from art import logo, vs

print(logo)
score = 0

a = data[randint(0, 49)]
nameA = a["name"]
countryA = a["country"]
infoA = a["description"]
followerA = a["follower_count"]
A = f"{nameA}, a {infoA}, from {countryA}"

end = True
while end:
    print("*If followers of A and B are same means A is same as B then no score will be added but game will continue.")
    
    print(f"Compare A: {A}")

    print(vs)

    b = data[randint(0, 49)]
    nameB = (b["name"])
    countryB = (b["country"])
    infoB = (b["description"])
    followerB = b["follower_count"]
    B = f"{nameB}, a {infoB}, from {countryB}"
    print(f"Against B: {B}")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if followerA > followerB and guess == "a":
        score += 1
        print(f"That's right. Score {score}")
        followerA = followerB
        A = B
    elif followerB > followerA and guess == "b":
        score += 1
        print(f"That's right. Score {score}")
        followerA = followerB
        A = B
    elif followerA > followerB and guess == "b":
        print(f"Sorry that's wrong. Final score {score}")
        end = False
    elif followerB  > followerA and guess == "a":
        print(f"Sorry that's wrong. Final score {score}")
        end = False
        
############################################################

## For better experience use below code in replit.com

# from random import randint
# from game_data import data
# from art import logo, vs
# from replit import clear

# print(logo)
# score = 0

# a = data[randint(0, 49)]
# nameA = a["name"]
# countryA = a["country"]
# infoA = a["description"]
# followerA = a["follower_count"]
# A = f"{nameA}, a {infoA}, from {countryA}"

# end = True
# while end:
#     print("*If followers of A and B are same means A is same as B then no score will be added but game will continue.")
    
#     print(f"Compare A: {A}")

#     print(vs)

#     b = data[randint(0, 49)]
#     nameB = (b["name"])
#     countryB = (b["country"])
#     infoB = (b["description"])
#     followerB = b["follower_count"]
#     B = f"{nameB}, a {infoB}, from {countryB}"
#     print(f"Against B: {B}")

#     guess = input("Who has more followers? Type 'A' or 'B': ")

#     if followerA > followerB and guess == "a":
#         score += 1
#         clear()
#         print(logo)
#         print(f"That's right. Score {score}")
#         followerA = followerB
#         A = B
#     elif followerB > followerA and guess == "b":
#         score += 1
#         clear()
#         print(logo)
#         print(f"That's right. Score {score}")
#         followerA = followerB
#         A = B
#     elif followerA > followerB and guess == "b":
#         clear()
#         print(logo)
#         print(f"Sorry that's wrong. Final score {score}")
#         end = False
#     elif followerB  > followerA and guess == "a":
#         clear()
#         print(logo)
#         print(f"Sorry that's wrong. Final score {score}")
#         end = False
