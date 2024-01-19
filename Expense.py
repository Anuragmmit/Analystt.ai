import datetime
import pandas as pd

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = datetime.date.today()

    expense_data.append({"date": date, "category": category, "amount": amount})
    print("Expense added successfully!")

def view_expenses():
    df = pd.DataFrame(expense_data)
    print(df)

def view_spending_patterns():
    df = pd.DataFrame(expense_data)

    # Group expenses by category and calculate total spending
    spending_by_category = df.groupby("category")["amount"].sum()
    print("Total spending by category:\n", spending_by_category)

    # Calculate daily spending
    daily_spending = df.groupby("date")["amount"].sum()
    print("\nDaily spending:\n", daily_spending)

expense_data = []

while True:
    print("\nExpense Tracker Menu")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View spending patterns")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_spending_patterns()
    elif choice == "4":
        break
    else:
        print("Invalid choice")