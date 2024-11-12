import csv , json , os, time
import expensesClass as ex



def save_to_csv(file_path = "expenses.csv"):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in ex.all_Expenses:
            writer.writerows([row])

def load_from_csv(file_path = "expenses.csv"):
    ex.all_Expenses = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for row in reader:
            ex.all_Expenses.append(row)
        return ex.all_Expenses

def save_to_json(file_path= "categories.json"):
    with open(file_path,"w") as file:
        json.dump(ex.all_categories, file, indent=3)

def load_from_json(file_path = "categories.json"):
    ex.all_categories = {}
    with open(file_path, "r") as file:
        try:
            if os.path.getsize("categories.json") == 0:
                print("The JSON file is empty. No data to load.")
                ex.all_categories = {}  # Continue as an empty dictionary
                return
        except FileNotFoundError:
            print("The file was not found.")
        except:
            ex.all_categories = json.load(file)
            return ex.all_categories


def show_expenses():
    choice = input("1. show all expenses  or    2. show by category. Enter 1 or 2: ")
    if choice == "1":
        print("Items Bougth          Price          Date")
        for expense in ex.all_Expenses:
            print(f"{expense[0]}             {expense[1]}             {expense[2]}\n")
    elif choice == "2":
        for key, value in ex.all_categories.items():
            print(f"{key} : {value}\n")
    else:
        print("invalid choice")

def calculate_expense():
    choice = input("How do you group your expenses ? time range(t) or category(c): ").lower()
    if choice == "t":
        pass

    elif choice == "c":
        choice2 = input("for which category do want to calculate your expenses?  ").capitalize()
        if choice2 in ex.allcategories:
            pass
        else:
            print("Sorry that category was not found")
            print("Calculating expenses for all categories...")
            time.sleep(2)
            total_expenses = 0
            for expense in ex.all_Expenses.values():
                total_expenses += sum(items["Amount"] for items in expense)
                print(f"{total_expenses} CFA")
            
    else:
            print("You didn't enter a valid response")