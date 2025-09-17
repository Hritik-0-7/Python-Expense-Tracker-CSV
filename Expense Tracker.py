import csv
import datetime
import os

CSV_FILE = 'expenses.csv'
FIELDNAMES = ['Date', 'Category', 'Description', 'Amount']

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(FIELDNAMES)

def add_expense():
    print("\n--- Add a New Expense ---")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    category = input("Enter the category (e.g., Food, Transport, Bills): ")
    description = input("Enter a brief description: ")
    
    while True:
        try:
            amount = float(input("Enter the amount: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")

    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            'Date': date,
            'Category': category,
            'Description': description,
            'Amount': f"{amount:.2f}"
        })
        
    print("\n Expense added successfully!")

def view_expenses():
    print("\n--- All Expenses ---")
    total_expenses = 0.0
    
    try:
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            expenses = list(reader)
            
            if not expenses:
                print("No expenses recorded yet. Start by adding one!")
                return

            print(f"{header[0]:<12} | {header[1]:<15} | {header[2]:<30} | {header[3]:>10}")
            print("-" * 75)

            for row in expenses:
                if len(row) == len(FIELDNAMES):
                    date, category, description, amount = row
                    print(f"{date:<12} | {category:<15} | {description:<30} | ${float(amount):>9.2f}")
                    total_expenses += float(amount)
                else:
                    print(f"Skipping malformed row: {row}")

            print("-" * 75)
            print(f"{'Total Expenses:':<60} ${total_expenses:>9.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet. The file will be created when you add your first expense.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    initialize_csv()
    
    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
