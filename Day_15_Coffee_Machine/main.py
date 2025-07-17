MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

# TODO #1.1 Create a function to print resources
def resources_report():
    """A function to display resources remaining in the machine, reads global resources dict and prints out the keys and
    their associated values with UOM added"""
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.title()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        else:
            print(f"{key.title()}: ${resources[key]}")

#TODO 2.1 Create a function to check resources against order
def resource_check(product_recipe):
    """A function to check if there are sufficient resources to make the order. Reads global resources dict and takes ingredients from menu dict as input (based on user choice). Returns True or False based on availability of resources."""
    for key in resources:
        if key in product_recipe:
            if product_recipe[key] > resources[key]:
                print(f"Sorry there is not enough {key}.")
                return False
    return True

# TODO #3.1 Create a function to insert and count coins and check if enough have been inserted
def coin_count():
    """A function to take the input for coins. Asks user to input the coin values and converts them into a single dollar value. Returns converted value."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total_coins = quarters + dimes + nickles + pennies
    return total_coins

def payment_check(product_price):
    """Function that checks if sufficient payment has been made to process the oder. Takes cost from MENU dict as input, reads payment global variable. Returns False if the payment made is > price or returns profit variable and prints out change if applicable"""
    profit = 0
    if payment < product_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif payment == product_price:
        profit = product_price
        return profit

    if payment > product_price:
        change = round(payment - product_price, 2)
        profit = product_price
        print(f"Here is ${change:.2f} in change.")
        return profit

# TODO #4.1 Create coffee brewing function
def make_coffee():
    """ A function that updates resources dict based on menu dict ingredients. Reads resources dict, menu dict and user_choice from global scope. Prints out the finalised user order."""
    for key in resources:
        if key in MENU[user_choice]["ingredients"]:
            resources[key] -= MENU[user_choice]["ingredients"][key]
    print(f"Here is your {user_choice}. Enjoy!")

# TODO #1: Take user input for orders, include a way to print a resources report, switch the coffee machine off
machine_on = True
resources["money"] = 0
while machine_on:
    user_choice = input("What would you like? (espresso / latte / cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        resources_report()
#TODO #2: Check resources are sufficient for the selected brew , reject the order if insufficient resources
    else:
        sufficient_resources = resource_check(MENU[user_choice]["ingredients"])
# TODO #3: If there are enough resources, process coins -  check that enough coins have been inserted, if insufficient coins reject the order
        if sufficient_resources:
            payment = coin_count()
            sufficient_payment = payment_check(MENU[user_choice]["cost"])
# TODO #4: If transaction is successful deduct the ingredients and serve the coffee, offer change if too many coins inserted
        if sufficient_resources and sufficient_payment:
            resources["money"] += sufficient_payment
            make_coffee()
