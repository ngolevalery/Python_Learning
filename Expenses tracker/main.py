import expensesClass as ex
import functions as fxn
running = True

while running:
    print("Expense Tracker Menu")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. Calculate expenses")
    print("4. view expense by category")
    print("5. Show all time expenses")

    choice = input("Enter your choice: ")

    fxn.load_from_csv()
    fxn.load_from_json()
    
    if choice == "1":
        new_expense = ex.Expenses.add_expense_details()
        ex.Expenses.add_expenses(new_expense)
        ex.Expenses.get_expense_by_category(new_expense)
        fxn.save_to_csv()
        fxn.save_to_json()

    elif choice == "2": 
        fxn.show_expenses()

    elif choice == "3":
        fxn.calculate_expense(ex.all_categories)

    elif choice == "4":
        ex.Expenses.get_expense_by_category()

    elif choice == "5":
        running = False
    

