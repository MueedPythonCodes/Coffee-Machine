
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



flag = True
money = 0


def make_coffee(user_desire,money,resources):
    sed = MENU[user_desire]["ingredients"]
    for key,value in sed.items():
        if key in resources:
            if resources[key] >= value:
                resources[key] -= value
            else:
                return -1
                
    money += MENU[user_desire]["cost"]   
    # print(resources)
    return money       
            




while flag:
    try:
        user_desire = input("What would you like? (espresso,latte,cappuccino): ").lower()
        if user_desire == "report":
            for key,value in resources.items():
                print(f"{key.capitalize()}: {value}")
            print(f"Money: ${money}")

        elif user_desire == "latte" or user_desire == "espresso" or user_desire == "cappuccino":
            print("Please insert coins.")
            quarters = int(input("How many quarters?")) * 0.25
            dimes = int(input("How many dimes?")) * 0.10
            nickels = int(input("How many nickles?")) * 0.05
            pennies = int(input("How many pennies?")) * 0.01
            total = quarters+dimes+nickels+pennies
            # print(f"Total amount user paid is {total}")

            if total > MENU[user_desire]["cost"]:
                # print(MENU[user_desire]["cost"])
                coffee_coins = make_coffee(user_desire,money,resources)
                if coffee_coins == -1:
                    print(f"Sorry the Coffee Machine is out of resources.")
                    break
                else:
                    money = coffee_coins
                    total = total - MENU[user_desire]["cost"]
                    print(f"Here is ${round(total,2)} in change!")
                    print(f"Here is your {user_desire}.Enjoy!☕🪶")
        
        elif user_desire == "off":
            print("Oops! Sorry.The Coffe Machine is turned off.")
            break

        else:
            print("Please enter a valid entry")

    except:
        print("There might be some error in your input please write Credentials Carefully!")
