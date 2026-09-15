expenses = []

def add_expense(amount=None, description=None):
    if amount is None:
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

    if description is None:
        description = input("Enter expense description: ")

    expense = {
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print(f"Expense added: {description} - GHS {amount:.2f}")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- Expense List ---")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['description']} - GHS {expense['amount']:.2f}")

def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: GHS {total:.2f}")

def delete_expenses():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()
    while True:
        try:
            index = int(input("Enter the number of the expense to delete (or 0 to cancel): "))
            if index == 0:
                print("Deletion cancelled.")
                return
            if 1 <= index <= len(expenses):
                deleted_expense = expenses.pop(index - 1)
                print(f"Deleted expense: {deleted_expense['description']} - GHS {deleted_expense['amount']:.2f}")
                return
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(expenses)}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Select an option (1-5): ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        total_expenses()
    elif choice == '4':
        delete_expenses()
    elif choice == '5':
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-5).")    