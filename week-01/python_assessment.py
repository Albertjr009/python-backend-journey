import json
import os

inventory = []

if os.path.exists("inventory_data.json"):
    with open("inventory_data.json", "r") as file:
        inventory = json.load(file)
        print("Inventory data loaded successfully.")
else:
    print("No existing inventory data found. Starting with an empty inventory.")
    
#Add Product Function
def add_product():
    print("\n--- Add a New Product ---")

    while True:
        name = input("Enter product name: ")

        if name.strip() == "":
            print("Product name cannot be empty. Please enter a valid name.")
            continue

        name_exists = False
        for item in inventory:
            if item["name"].lower() == name.lower():
                name_exists = True
                break

        if name_exists:
            print(f"Product '{name}' already exists in the inventory.")
            continue

        break

    while True:
        try:
            price = float(input("Enter product price (GHS): "))
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the price.")

    while True:
        try:
            quantity =  int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please enter a valid quantity.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the quantity.")
    
    # Packaging all the details into a single "Product Card"
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    inventory.append(product)
    print(f"Success! {name} has been added.")

    with open("inventory_data.json", "w") as file:
        json.dump(inventory, file, indent=4)

#View Function
def view_products():
    print("\n--- Current Inventory ---")
    
    # If the notebook is empty
    if len(inventory) == 0:
        print("Your inventory is empty.")
    
    # Otherwise, loop through and print each product card
    for product in inventory:
        print(f"Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}")

#Delete function
def delete_product():
    print("\n--- Delete a Product ---")
    

    target_name = input("Enter the name of the product to delete: ").strip()
    
    for product in inventory:
        if product["name"].lower() == target_name.lower():
            inventory.remove(product)
            print(f"Success: '{target_name}' has been deleted.")
            with open("inventory_data.json", "w") as file:
                json.dump(inventory, file, indent=4)
            return #
            

    print(f"Error: Product '{target_name}' not found in inventory.")

#Search function
def search_product():
    print("\n--- Search for a Product ---")
    
    # which product the user want to search for
    target_name = input("Enter the name of the product to search: ").strip()
    
    
    for product in inventory:
        # If the product name matches what the user typed...
        if product["name"].lower() == target_name.lower():
            
            print(f"Found: Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}")
            return 
            
    print(f"Error: Product '{target_name}' not found in inventory.")

#Update function
def update_product():
    print("\n--- Update a Product ---")
    target_name = input("Enter the name of the product to update: ").strip()

    for product in inventory:
        if product["name"].lower() == target_name.lower():
            print(f"Found: Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}") 

            new_name = input("Enter new product name (leave blank to keep current): ")
            new_price = input("Enter new product price (leave blank to keep current): ")
            new_quantity = input("Enter new quantity (leave blank to keep current): ")

            product["name"] = new_name if new_name else product["name"]
            product["price"] = new_price if new_price else product["price"]
            product["quantity"] = new_quantity if new_quantity else product["quantity"]

            with open("inventory_data.json", "w") as file:
                json.dump(inventory, file, indent=4)

            print(f"Success: '{target_name}' has been updated.")
            return

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')


while True:
    print("\n===== ALBERT'S INVENTORY =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Search Product") 
    print("5. Update Product")
    print("6. Clear Screen")
    print("7. Exit")
    
    choice = input("Choose an option (1-7): ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        search_product()
    elif choice == "5":
        update_product()
    elif choice == "6":
        clear_screen()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please type 1, 2, 3, 4, 5, 6 or 7.")
 