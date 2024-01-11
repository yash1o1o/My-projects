import os
import json
from datetime import datetime

# File to store expense data
DATA_FILE = "expense_data.json"

# Load expense data from file or create an empty dictionary
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        expense_data = json.load(file)
else:
    expense_data = {}

def save_data():
    # Save expense data to file
    with open(DATA_FILE, 'w') as file:
        json.dump(expense_data, file, indent=2)

def record_expense():
    # Record daily expenses
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter expense category (food, transportation, entertainment, etc.): ")

    # Validate category
    if category.lower() not in ["food", "transportation", "entertainment", "other"]:
        print("Invalid category. Expense not recorded.")
        return

    # Record expense with timestamp
    date_today = datetime.today().strftime('%Y-%m-%d')
    if date_today not in expense_data:
        expense_data[date_today] = []

    expense_data[date_today].append({
        "amount": amount,
        "description": description,
        "category": category.lower()
    })

    print("Expense recorded successfully!")

def monthly_summary():
    # Show monthly expense summary
    month = input("Enter the month (YYYY-MM) for summary: ")
    total_expenses = 0

    if month in expense_data:
        print("\nMonthly Summary for {}: ".format(month))
        for expense in expense_data[month]:
            print("Category: {}, Amount: ${:.2f}, Description: {}".format(
                expense["category"].capitalize(), expense["amount"], expense["description"]
            ))
            total_expenses += expense["amount"]
        print("\nTotal Expenses for {}: ${:.2f}".format(month, total_expenses))
    else:
        print("No data available for the specified month.")

def category_wise_expenditure():
    # Show category-wise expenditure
    category = input("Enter the expense category for analysis: ")
    total_category_expenses = 0

    for expenses in expense_data.values():
        for expense in expenses:
            if expense["category"] == category.lower():
                total_category_expenses += expense["amount"]

    print("\nCategory-wise Expenditure for {}: ${:.2f}".format(category.capitalize(), total_category_expenses))

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Record Expense")
        print("2. Monthly Summary")
        print("3. Category-wise Expenditure")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            record_expense()
            save_data()
        elif choice == "2":
            monthly_summary()
        elif choice == "3":
            category_wise_expenditure()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
