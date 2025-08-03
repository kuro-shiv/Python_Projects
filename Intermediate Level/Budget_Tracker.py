#loop for few option in budget tracker with functions and options to input data and display it


# Initialize lists to store income and expenses
class BudgetTracker:
    def run(self):
        while True:
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View Balance")
            print("4. Transaction History")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_income()
            elif choice == '2':
                self.add_expense()
            elif choice == '3':
                self.view_balance()
            elif choice == '4':
                self.view_transactions()
            elif choice == '5':
                print("Exiting Budget Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            print("\n")

# Budget Tracker Class
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    # Methods to add income, add expense, view balance, and view transactions
    #add income function
    def add_income(self):
        amount = float(input("Enter income amount: "))
        source = input("Enter income source: ")
        
        self.balance += amount
        self.transactions.append(f"Income: {source} - ₹{amount:.2f}")
        print(f"Income of ₹{amount:.2f} from {source} added successfully.")
    #add expense function
    def add_expense(self):
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        self.balance -= amount
        self.transactions.append(f"Expense: {category} - ₹{amount:.2f}")
        print(f"Expense of ₹{amount:.2f} in {category} added successfully.")
    # View balance function
    def view_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")
    # View transactions function
    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)


# Create an instance of BudgetTracker and run it

budget_tracker = BudgetTracker()
budget_tracker.run()