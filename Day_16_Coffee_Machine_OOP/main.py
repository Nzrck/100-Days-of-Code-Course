from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
payment_processor = MoneyMachine()

def main():

    coffee_machine_functions = {
        "report": resources_report,
        "latte": coffee_process,
        "cappuccino": coffee_process,
        "espresso": coffee_process,
    }

    while True:
        user_input = input(f"What would you like? {menu.get_items()}: ").lower()
        if user_input == "off":
            return
        elif user_input in coffee_machine_functions:
            coffee_machine_functions[user_input](user_input)
        else:
            print("Sorry this item is not available.")

def resources_report(_):
    coffee_machine.report()
    payment_processor.report()

def coffee_process(input):
    if menu.find_drink(input):
        order = menu.find_drink(input)
        if coffee_machine.is_resource_sufficient(order):
            if payment_processor.make_payment(order.cost):
                coffee_machine.make_coffee(order)

main()
