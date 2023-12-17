# 100 days of code: Day 15: Coffee Machine
#This is the final code
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

machine_off = False
profit = 0


def calc_money(quarter, dime, nickel, penny):
    quarter_val = quarter * 25
    dime_val = dime * 10
    nickel_val = nickel * 5
    penny_val = penny
    return (quarter_val + dime_val + nickel_val + penny_val) / 100


def reduce_resources(product):
    for ingredient in MENU[product]["ingredients"]:
        resources[ingredient] -= MENU[product]["ingredients"][ingredient]
        # print(ingredient, resources[ingredient])


def check_resources(product):
    for ingredient in MENU[product]["ingredients"]:
        # print(MENU[product]["ingredients"][ingredient], "-", resources[ingredient])
        if MENU[product]["ingredients"][ingredient] > resources[ingredient]:
            message = f"Sorry, there is not enough {ingredient}"
            return message
        else:
            return "yes"


while not machine_off:
    # prompt
    user_wants = input(
        "What would you like? (espresso/latte/cappuccino):").lower()
    if user_wants == "espresso" or user_wants == "latte" or user_wants == "cappuccino":
        is_left = check_resources(user_wants)
        if is_left == "yes":
            num_quarters = int(input("How many quarters?"))
            num_dimes = int(input("How many dimes?"))
            num_nickels = int(input("How many nickels?"))
            num_pennies = int(input("How many pennies?"))
            total_money = calc_money(num_quarters, num_dimes, num_nickels,
                                     num_pennies)
            money_needed = MENU[user_wants]["cost"]
            if money_needed <= total_money:
                if total_money > money_needed:
                    print(f"Change: $ {round((total_money - money_needed), 2)}")
                reduce_resources(user_wants)
                print(f"Here is your {user_wants}. Enjoy!")
                profit += money_needed
            else:
                print("Sorry, that's not enough money. Money refunded.")
        else:
            print(is_left)

    elif user_wants == "off":
        machine_off = True

    elif user_wants == "report":
        water_num = resources["water"]
        milk_num = resources["milk"]
        coffee_num = resources["coffee"]
        print(f"Water:{water_num}ml")
        print(f"Milk: {milk_num}ml")
        print(f"Coffee: {coffee_num}g")
        print(f"Revenue: ${profit}")
