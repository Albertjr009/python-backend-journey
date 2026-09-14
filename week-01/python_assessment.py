import sys

# This empty list will act as my inventory database
inventory = []

def add_product():
    print("\n--- Add a New Product ---")
    
    # 1. Asking the user for details
    name = input("Enter product name: ")
    price = input("Enter product price (GHS): ")
    quantity = input("Enter quantity: ")
    
    # 2. Packaging all the details into a single "Product Card"
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    # 3. Putting the product card inside the inventory notebook
    inventory.append(product)
    print(f"Success! {name} has been added.")

def view_products():
    print("\n--- Current Inventory ---")
    
    # If the notebook is empty, tell the user
    if len(inventory) == 0:
        print("Your inventory is empty.")
    
    # Otherwise, loop through and print each product card
    for product in inventory:
        print(f"Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}")

def delete_product():
    print("\n--- Delete a Product ---")
    
    # 1. Which product does the user want to delete
    target_name = input("Enter the name of the product to delete: ").strip()
    
    # 2. Search through the inventory to find it
    for product in inventory:
        # If the product name matches what the user typed...
        if product["name"].lower() == target_name.lower():
            # 3. Remove it from the list
            inventory.remove(product)
            print(f"Success: '{target_name}' has been deleted.")
            return #
            

    print(f"Error: Product '{target_name}' not found in inventory.")

def search_product():
    print("\n--- Search for a Product ---")
    
    # 1. which product they want to search for
    target_name = input("Enter the name of the product to search: ").strip()
    
    
    for product in inventory:
        # If the product name matches what the user typed...
        if product["name"].lower() == target_name.lower():
            
            print(f"Found: Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}")
            return 
            
    print(f"Error: Product '{target_name}' not found in inventory.")

while True:
    print("\n===== ALBERT'S INVENTORY =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Search Product") 
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        search_product()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please type 1, 2, 3, 4, or 5.")
    print("3. Delete Product")      
    print("4. Search Product")  
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        delete_product()   
    elif choice == "4":
        search_product()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please type 1, 2, 3, 4, or 5.")
