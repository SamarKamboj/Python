from cryptography.fernet import Fernet, InvalidToken
import pyperclip
import sys, json, os


try:
    key = int(input("1 Generate Key\n2 Enter Key\n"))
except ValueError:
    sys.exit("Please enter a valid number!")

if key == 1:
    key = Fernet.generate_key()
    pyperclip.copy(key.decode())
    print("Key Copied!")
elif key == 2:
    key = input("KEY: ").encode()
else:
    sys.exit("Invalid input!")

os.system("cls")

try:
    cypher = Fernet(key)
except [ValueError, AttributeError]:
    sys.exit("Invalid key!")

if not os.path.isfile("data.json"):
    with open("data.json", 'w') as file:
        json.dump(dict(), file)


def main():
    try:    
        option = int(input("1 Encrypt\n2 Decrypt\n3 New Key\n"))
    except ValueError:
        sys.exit("Please enter a valid number")
    else:
        os.system("cls")

    if option == 1:
        # TODO Ask and store --> Done
        while True:
            print("Please remember name so that you can access data!")
            name = input("NAME: ").lower()

            email = input("EMAIL: ")

            password = cypher.encrypt(input("PASSWORD: ").encode())
            password = password.decode()

            store(name, email, password)

            q = input("Do you want to add more? (y/n)").lower()
            if q == 'n' or q == 'no':
                break

    elif option == 2:
        # TODO Ask for name and give back it's pass
        name = input("NAME: ")
        email = input("EMAIL: ")

        password = access(name, email)
        if password:
            pyperclip.copy(password)
            os.system("cls")
            print("Pass Copied!")
        else:
            print("Invalid EMAIL!")

    elif option == 3:
        # TODO Generate key and update each password to that key
        new_key = Fernet.generate_key()
        new_cypher = Fernet(new_key)

        change_key(new_cypher)

        pyperclip.copy(new_key.decode())
        print("Key Copied!")

    else:
        sys.exit("Please enter a valid number")


def store(name, email, password):
    data = format_data(name, email, password)
    json_data = json.dumps(data, indent=4)

    with open("data.json", 'w') as file:
        file.write(json_data)


def format_data(name, email, password):
    with open("data.json") as file:
        data = json.load(file)

    if name not in data:
        data[name] = list()

    for names in data[name]:
        if email == names["email"]:
            new_pass = input("Email already exists. Do you want to change password (y/n)?").lower()
            if new_pass == 'y' or new_pass == 'yes':
                names["pass"] = password
                return data
            else:
                return data

    data[name].append({"email": email, "pass": password})
    return data


def access(name, email):
    with open("data.json") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            os.system("cls")
            sys.exit("NO DATA AVAILABLE")

    if name not in data:
        sys.exit("NO DATA AVAILABLE!")

    for names in data[name]:
        if email == names["email"]:
            try:
                password = cypher.decrypt(names["pass"].encode())
            except InvalidToken:
                sys.exit("Invalid Key!")
            else:
                return password.decode()

    return None


def change_key(new_cypher):
    with open("data.json") as file:
        data = json.load(file)

    for names in data:
        for detail in data[names]:
            try:
                password = cypher.decrypt(detail["pass"].encode())
            except InvalidToken:
                sys.exit("Invalid Key!")

            new_password = new_cypher.encrypt(password)
            detail["pass"] = new_password.decode()

    with open("data.json", 'w') as file:
        file.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()
