import sys

# This empty list will act as my inventory database
inventory = []

def add_product():
    print("\n--- Add a New Product ---")
    
    # Asking the user for details
    name = input("Enter product name: ")
    price = input("Enter product price (GHS): ")
    quantity = input("Enter quantity: ")
    
    # Packaging all the details into a single "Product Card"
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    # Putting the product card inside the inventory notebook
    inventory.append(product)
    print(f"Success! {name} has been added.")

def view_products():
    print("\n--- Current Inventory ---")
    
    # If the notebook is empty
    if len(inventory) == 0:
        print("Your inventory is empty.")
    
    # Otherwise, loop through and print each product card
    for product in inventory:
        print(f"Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}")

def delete_product():
    print("\n--- Delete a Product ---")
    
    # Which product does the user want to delete
    target_name = input("Enter the name of the product to delete: ").strip()
    
    # Search through the inventory to find it
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
    
    # which product the user want to search for
    target_name = input("Enter the name of the product to search: ").strip()
    
    
    for product in inventory:
        # If the product name matches what the user typed...
        if product["name"].lower() == target_name.lower():
            
            print(f"Found: Name: {product['name']} | Price: GHS {product['price']} | Qty: {product['quantity']}")
            return 
            
    print(f"Error: Product '{target_name}' not found in inventory.")


#the Update function
def update_product():
    print("\n--- Update a Product ---")
    #learnt to target the product by name and update its details
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

            print(f"Success: '{target_name}' has been updated.")
            return

while True:
    print("\n===== ALBERT'S INVENTORY =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")
    print("4. Search Product") 
    print("5. Update Product")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")
    
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please type 1, 2, 3, 4, 5, or 6.")
    print("1. Add Product")
    print("2. View Products")
    print("3. Delete Product")      
    print("4. Search Product")  
    print("5. Update Product")
    print("6. Exit")
    
    choice = input("Choose an option (1-6): ")
    
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
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please type 1, 2, 3, 4, 5, or 6.")
