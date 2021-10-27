#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

pg = True
while pg == True:
    print("Welcome to the PyPassword Generator!")

    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))

    let = []
    for x in range(0, nr_letters):
        let += random.choice(letters)  # Angela's method

    for y in range(0, nr_numbers):
        let += random.choice(numbers)  # Angela's method

    for z in range(0, nr_symbols):
        let += random.choice(symbols)  # Angela's method

    random.shuffle(let)

    password = ''
    for a in let:
        password += a
    print(f"Your Password is: {password}")

    end = int(input("Type 0 to Exit or Any number to Generate Password Again\n"))
    if end == 0:
        pg = False
