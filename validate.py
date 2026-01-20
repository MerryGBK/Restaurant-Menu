
inventory = {}

def add_ingredient():
    name = input("Enter the ingredient name: ").strip().lower()
    if not name:
        print("Ingredient name cannot be empty.")
        return
    quantity = input("Enter the quantity (e.g., '10 kg', '2 litres'): ").strip()
    if not quantity:
        print("Quantity cannot be empty.")
        return
    inventory[name] = quantity
    print(f"Ingredient '{name}' added with quantity '{quantity}'.")

def view_inventory():
    if not inventory:
        print("Inventory is currently empty.")
    else:
        print("\nCurrent Inventory:")
        for ingredient, quantity in inventory.items():
            print(f"- {ingredient.title()}: {quantity}")

def update_ingredient():
    name = input("Enter the name of the ingredient to update: ").strip().lower()
    if name not in inventory:
        print(f"Ingredient '{name}' not found in inventory.")
        return
    new_quantity = input("Enter the new quantity: ").strip()
    if not new_quantity:
        print("Quantity cannot be empty.")
        return
    inventory[name] = new_quantity
    print(f"Ingredient '{name}' updated to '{new_quantity}'.")

def search_ingredient():
    name = input("Enter the ingredient to search for: ").strip().lower()
    if name in inventory:
        print(f"{name.title()} is available with quantity: {inventory[name]}")
    else:
        print(f"Ingredient '{name}' not found in inventory.")

def display_menu():
    print("\n--- Bakery Inventory Menu ---")
    print("1. Add Ingredient")
    print("2. View Inventory")
    print("3. Update Ingredient")
    print("4. Search Ingredient")
    print("5. Exit")

def main():
    print("Welcome to the Sweet Surrender Bakery Inventory System!")
    while True:
        display_menu()
        choice = input("Enter your choice (1–5): ").strip()
        
        if choice == '1':
            add_ingredient()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_ingredient()
        elif choice == '4':
            search_ingredient()
        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
