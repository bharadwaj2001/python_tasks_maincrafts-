import csv
from datetime import datetime

# Add expense with category
def add_expense(desc, amount, category):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, datetime.now().strftime("%Y-%m-%d")])

# View all expenses
def view_expenses():
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            print(row)

# Search expenses by category

def search_category(category):
    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # skip empty rows
            if not row:
                continue
            # check if row has at least 3 columns
            if len(row) > 2 and row[2].strip().lower() == category.strip().lower():
                print(row)

# Monthly total
def monthly_total(month):
    results = []

    with open("expenses.csv", "r") as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header

        for row in reader:
            try:
                if row[3].startswith(month):  # Match "2025-11"
                    results.append(row)
            except Exception:
                continue  # Skip bad rows

    if results:
        print(f"Expenses for {month}:")
        for r in results:
            print(r)
    else:
        print(f"No expenses found for {month}.")



# ✅ Continuous Menu Loop
while True:
    n = input("\nPlease select:\n1. Add Expenses\n2. View Expenses\n3. Search Category\n4. Monthly Expenses\n5. Exit\n")

    match n:
        case "1" | "Add Expenses":
            item, amount, category = map(str.strip, input("Enter (item, amount, category): ").split(","))
            add_expense(item, amount, category)
            print("✅ Expense Added Successfully!")

        case "2" | "View Expenses":
            view_expenses()

        case "3" | "Search Category":
            category = input("Enter Category Name: ")
            search_category(category)

        case "4" | "Monthly Expenses":
            month = input("Enter Month Number with Year (2025-11)")
            monthly_total(month)

        case "5" | "Exit":
            print("👋 Exiting Program... Bye!")
            break   # <-- Program stops here

        case _:
            print("❌ Please select a valid option")
