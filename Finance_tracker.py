"""
Afnan Ali.
4.13.2025
Finance Tracker Program
-----------------------
This simple program allows users to track their personal finances by:
- Adding income and expense transactions
- Viewing all saved transactions
- Calculating total income, expenses, and current balance

All data is saved in a file called 'budget.txt'.

"""


# Adds a transaction (income or expense) to the file
def add_transaction():
    categories = ['food', 'transport', 'rent', 'grocery', 'shopping', 'entertainment', 'other']
    t_category = None

    # Ask user for type of transaction
    t_type = input("Income Or Expense : ").lower()
    while t_type != "income" and t_type != "expense":
        t_type = input("Income Or Expense : ").lower()

    # If it's an expense, ask for category too
    if t_type == "expense":
        t_amount = 0
        while t_amount <= 0:
            t_amount = float(input("Enter Amount : "))

        print("Choose a category : ")
        for i in categories:
            print("-", i)

        t_category = input("Enter Category : ")

        if t_category not in categories:
            print("Invalid category !")

    else:
        # For income, just ask for amount
        t_amount = 0
        while t_amount <= 0:
            t_amount = float(input("Enter Amount : "))

    # Save transaction in the file
    with open("budget.txt", "a") as file:
        file.write(f" Type - {t_type} \n")
        file.write(f" Amount - ${t_amount}\n")
        if t_category:
            file.write(f" Category - {t_category}\n")
        file.write("-" * 25 + "\n")

    print("\nTransaction added successfully!")


# Displays the contents of the budget file
def view_transactions():
    with open("budget.txt", "r") as file:
        print(f"\n{file.read()}")


# Calculates and shows total income, expenses, and balance
def show_balance():
    total_income = 0
    total_expenses = 0

    # Read all lines from the file
    with open("budget.txt", "r") as file:
        lines = file.readlines()

    # Loop through lines and calculate totals
    for i in range(len(lines)):
        if "Type - income" in lines[i]:
            amount_line = lines[i + 1]
            amount = float(amount_line.strip().split("$")[1])
            total_income += amount

        elif "Type - expense" in lines[i]:
            amount_line = lines[i + 1]
            amount = float(amount_line.strip().split("$")[1])
            total_expenses += amount

    balance = total_income - total_expenses

    print(f"Your balance is ${balance}.")
    print(f"Income - ${total_income}.")
    print(f"Expenses - ${total_expenses}.")


# Main menu loop
def main():
    print("\nWELCOME TO YOUR FINANCE TRACKER!")
    print("\nChoose an option:\n1. Add Transaction\n2. View All Transactions\n3. Show Total Balance\n4. Exit\n")

    choice = int(input(">"))

    while choice != 4:
        if choice == 1:
            add_transaction()
        elif choice == 2:
            view_transactions()
        elif choice == 3:
            show_balance()

        print("\nChoose an option:\n1. Add Transaction\n2. View All Transactions\n3. Show Total Balance\n4. Exit\n")
        choice = int(input("\n>"))


# Start the program
main()
