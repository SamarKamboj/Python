MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

moneySpent = 0
def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(moneySpent))


def coins():
    global amount
    print("Please Insert Coins")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    # Amount calculated after getting inputs
    amount = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)


def deductRe():
    resources["water"] -= ingredients["water"]
    resources["milk"] -= ingredients["milk"]
    resources["coffee"] -= ingredients["coffee"]


end = True
while end:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")
    if userInput == "off":
        end = False
    elif userInput == "report":
        report()
    elif userInput in MENU:
        coffeeCost = MENU[userInput]["cost"]
        moneySpent += coffeeCost
        ingredients = MENU[userInput]["ingredients"]

        # Check if resources are enough to make the coffee
        if ingredients["water"] <= resources["water"] and ingredients["milk"] <= resources["milk"] and ingredients["coffee"] <= resources["coffee"]:
            # Deduct resources
            deductRe()
            # Please insert coins
            coins()
            if coffeeCost <= amount:
                change = round((amount - coffeeCost), 2)
                print(f"Here is ${change} in change")
                print(f"Here is your {userInput}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry not enough resources.")
    else:
        print("Coffee not in list.")