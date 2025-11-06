import csv

def add_expense(desc, amount):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

def view_expenses():
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if not row:
                continue
            print(f"Item: {row[0]}, Amount: ₹{row[1]}")

def total_expenses():
    total = 0
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if not row:
                continue
            total += int(row[1])
    print("Total Expenses: ₹", total)


# ✅ Continuous Menu Loop
while True:
    n = input("\nPlease select:\n1. Add Expenses\n2. View Expenses\n3. Total Expenses\n4. Exit\n")

    match n:
        case "1" | "Add Expenses":
            item, amount = map(str.strip, input("Enter item and amount (item,amount): ").split(","))
            add_expense(item, amount)
            print("✅ Expense Added Successfully!")

        case "2" | "View Expenses":
            view_expenses()

        case "3" | "Total Expenses":
            total_expenses()

        case "4" | "Exit":
            print("👋 Exiting Program... Bye!")
            break   # <-- Program stops here

        case _:
            print("❌ Please select a valid option")
import csv

def add_expense(desc, amount):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

def view_expenses():
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if not row:
                continue
            print(f"Item: {row[0]}, Amount: ₹{row[1]}")

def total_expenses():
    total = 0
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if not row:
                continue
            total += int(row[1])
    print("Total Expenses: ₹", total)


# ✅ Continuous Menu Loop
while True:
    n = input("\nPlease select:\n1. Add Expenses\n2. View Expenses\n3. Total Expenses\n4. Exit\n")

    match n:
        case "1" | "Add Expenses":
            item, amount = map(str.strip, input("Enter item and amount (item,amount): ").split(","))
            add_expense(item, amount)
            print("✅ Expense Added Successfully!")

        case "2" | "View Expenses":
            view_expenses()

        case "3" | "Total Expenses":
            total_expenses()

        case "4" | "Exit":
            print("👋 Exiting Program... Bye!")
            break   # <-- Program stops here

        case _:
            print("❌ Please select a valid option")
