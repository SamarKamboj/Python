logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    word = ""
    
    # Looping in text and modifing according to user direction
    for char in start_text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            if direction == 'encode':
                for x in range(shift_amount):
                    letter_index += 1
                    if letter_index > 25:
                        letter_index = 0
            elif direction == 'decode':
                for x in range(shift_amount):
                    letter_index -= 1
                    if letter_index < 0:
                        letter_index = 25
            new_letter = alphabet[letter_index]
            word += new_letter  # Adding new letter in empty string 'word'
        else:
            word += char

    print(f"The {cipher_direction}d text is:",word)  # Printing the required text

end = True
while end:
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    end_of_game = input("Type 'yes' to continue or 'no' to exit.\n")
    if end_of_game == 'no':
        end = False
