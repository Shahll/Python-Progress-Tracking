def shop(money):
    money = int(money)
    user_basket = []
    flag = True
    shop_inventory = {
        'apples': {'price': 10, 'quantity': 5},
        'bananas': {'price': 15, 'quantity': 10},
        'oranges': {'price': 12, 'quantity': 3},
        'pears': {'price': 8, 'quantity': 7},
        'plums': {'price': 6, 'quantity': 2}
    }
    print("Available items\n")
    while flag :
        
        
        for item, details in shop_inventory.items():
            print(f"{item}: price - {details['price']}, quanitity - {details['quantity']} ")
        print("\nEnter a name of item or 'stop' to end you shopping")
        choice = input()
        
        if choice == "stop" or money == 0:
            flag = False
            
        if choice in shop_inventory:
            item_details = shop_inventory[choice]
            if item_details['quantity'] > 0 and item_details['price'] <= money:
                user_basket.append(choice)
                money -= item_details['price']
                item_details['quantity'] -= 1
                print(f"\nYou add {choice} in your basket and you still have {money} hryvnias left\n")
                
            elif item_details['quantity'] == 0:
                print(f"Im sorry but there are no more {choice} left")
                
            elif item_details['price'] > money:
                print(f"Im sorry, you dont have enough cash to buy {choice}, but you still have {money} hryvnias")
            
    print(f"\nYou bought this and still have {money} hryvnias:")   
    for fruit in set(user_basket):
        print(user_basket.count(fruit), fruit)
            
money = 100
shop(money)
