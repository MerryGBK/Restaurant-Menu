customer_name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")
address = input("Enter your address: ")

item1 = "Burger"
price1 = 5.00
item2 = "Pizza"
price2 = 8.00
item3 = "Pasta"
price3 = 7.50
item4 = "Salad"
price4 = 4.00
item5 = "Soda"
price5 = 1.50

total_cost = 0
while True:
    print("\n---Restaurant Menu---")
    print(f"1. {item1}: £{price1:.2f}")
    print(f"2. {item2}: £{price2:.2f}")
    print(f"3. {item3}: £{price3:.2f}")
    print(f"4. {item4}: £{price4:.2f}")
    print(f"5. {item5}: £{price5:.2f}")

    order_item = input("\nEnter the item order (or 'done' to finish): ").capitalize()
    
    if order_item == "Done":
        print(f"\nYour order cost is: £{total_cost:.2f}")
        print(f"Thank you for your order!")
        print(f"Your order will be delivered in 25 minutes to the address: {address}")
        break
    elif order_item == item1:
        quantity = int(input(f"How many {item1}s would you like to order? "))
        if quantity > 0:
            total_cost += price1 * quantity
            print(f"{quantity} {item1}(s) added to your order.")
        else:
            print("Please order at least 1 item.")
    elif order_item == item2:
        quantity = int(input(f"How many {item2}s would you like to order? "))
        if quantity > 0:
            total_cost += price2 * quantity
            print(f"{quantity} {item2}(s) added to your order.")
        else:
            print("Please order at least 1 item.")
    elif order_item == item3:
        quantity = int(input(f"How many {item3}s would you like to order? "))
        if quantity > 0:
            total_cost += price3 * quantity
            print(f"{quantity} {item3}(s) added to your order.")
        else:
            print("Please order at least 1 item.")
    elif order_item == item4:
        quantity = int(input(f"How many {item4}s would you like to order? "))
        if quantity > 0:
            total_cost += price4 * quantity
            print(f"{quantity} {item4}(s) added to your order.")
        else:            print("Please order at least 1 item.")
    elif order_item == item5:
        quantity = int(input(f"How many {item5}s would you like to order? "))
        if quantity > 0:
            total_cost += price5 * quantity
            print(f"{quantity} {item5}(s) added to your order.")
        else:
            print("Please order at least 1 item.")
    else:
        print("Invalid item. Please choose from the menu.")

