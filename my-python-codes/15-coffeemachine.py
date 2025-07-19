MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18}, "cost": 1.5
    },

    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5
    },

    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0
    }
}

resources = {
    "coffee": 1000,
    "milk": 2000,
    "water": 3000,
    "profit": 0
}

def check_sufficiency(coffee_type):                          #Just comparing the resource dict with chosen coffee ingred dict 
    for ing in resources:
        if ing == 'profit':
            continue
        elif resources[ing] < MENU[coffee_type]["ingredients"][ing]:    
            print(f"Sorry there isn't enough {ing}")      
            return False
        else:
            continue
    return True

def calculate_total():
    penny = float(input("Pennies: "))
    nickle = float(input("Nickels: "))
    dime = float(input("Dimes: "))
    quarters = float(input("Quarters: "))
    total= (penny * 0.01) + (nickle * 0.05) + (dime * 0.10) + (quarters * 0.25)
    return(round(total, 2))

def make_coffee(coffee_type):
    for ing in resources:
        if ing == 'profit':
            continue
        else:
            resources[ing] = resources[ing] - MENU[coffee_type]["ingredients"][ing]

def process(choice):
    sufficient = (check_sufficiency(choice))
    if sufficient == True:
        choice_cost = MENU[choice]['cost']
        print(f"The {choice} costs ${choice_cost}\nEnter the {choice} amount ${choice_cost} as pennies, nickles, dimes, quarters")
        total_paid = calculate_total()
        if total_paid < choice_cost:
            print("Sorry that's not enough money. Money refunded.")
            return 0
        elif total_paid >= choice_cost:
            resources['profit'] += round(choice_cost, 2)
            make_coffee(choice)
            if total_paid > choice_cost:
                print(f"Here's your balance amount: ${round(total_paid - choice_cost, 2)}")
            print(f"Here is your {choice} ☕. Enjoy!")
        else:
            print("Process Error")

def start():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == 'report':
            print(resources)
        elif choice == 'off':
            return 0
        elif choice in MENU:
            process(choice)
        else:
            ("Invalid Choice, Try Again.")
        print("\n")

start()























"""
for ingredient, amount in MENU[coffee_type]["ingredients"].items():
    if resources[ingredient] < amount:
        print(f"Sorry there isn't enough {ingredient}")
        return False

"""