#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

let = ''
for x in range(0, nr_letters):
  let += letters[random.randint(0, len(letters)-1)]

num = ''
for x in range(0, nr_numbers):
  num += numbers[random.randint(0, len(numbers)-1)]

sym = '' 
for x in range(0, nr_symbols):
  sym += symbols[random.randint(0, len(symbols)-1)]

print("Easy password: " + let + num + sym)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

let = []
for x in range(0, nr_letters):
  # let += letters[random.randint(0, len(letters)-1)]  # My method
  let += random.choice(letters)  # Angela's method

for y in range(0, nr_numbers):
  # let += numbers[random.randint(0, len(numbers)-1)]  # My method
  let += random.choice(numbers)  # Angela's method

for z in range(0, nr_symbols):
  # let += symbols[random.randint(0, len(symbols)-1)]  # My method
  let += random.choice(symbols)  # Angela's method

random.shuffle(let)

password = ''
for a in let:
  password += a

print("Hard password: " + password)