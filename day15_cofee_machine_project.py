from day15_cofee_machine_data import MENU,resources


def check_coins():
    """Processing coins"""
    print("Please insert the Coins")
    dollars=int(input("How many quarters?: ")) * 0.25
    dollars+=int(input("How many dimes?: ")) * 0.1
    dollars+=int(input("How many nickles?: ")) * 0.05
    dollars=int(input("How many pennies?: ")) * 0.01
    # do/llars=round(dollars,2)
    return dollars


def quantity(ingredients):
    """Checking whether resources are enough or not"""
    sufficient=True
    for key in ingredients:
        if ingredients[key]>=resources[key]:
            print(f"Coffee Machine does not have enough {key}")
            return False
    
    return sufficient



def successful_purchase(amount,menu):
    if amount>=menu['cost']:
        remaining=round(amount-menu["cost"],2)
        print(f"Here is ${remaining} in change.")
        global money
        money += MENU[user_input]['cost']
        return True
    else:
        print("You do not have enough money.Money refunded")
        return False



def start_making_cofee(user_input,ingreients):
    """This will cut off the required ingredients from  resources"""
    for key in ingredients:
        resources[key] -= ingredients[key]
    print(f"Here is your {user_input}. Enjoy!")



end=True
money=0
while end:
    user_input=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input=="off":
        end=False
    elif user_input=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Cofee: {resources['coffee']}g")
        print(f"Money: ${money}") 
    else:
        ingredients=MENU[user_input]['ingredients']
        if quantity(ingredients):
            amount=check_coins()
            if successful_purchase(amount,MENU[user_input]):
                start_making_cofee(user_input,ingredients)
