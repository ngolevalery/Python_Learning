import datetime

all_Expenses = []
all_categories = {}

class Expenses:
    def __init__(self,item, amount, category, date):
        self.item = item
        self.amount = amount
        self.category = category 
        self.date = date

    @classmethod
    def add_expense_details(cls): #Collects user input to create an Expenses instance
        item = input("What did you buy or paid for ? ") 
        amount = float(input("How much did this item cost ? "))
        date = input("When did you carry out the transaction mm/dd/yy ?  ")
        category = input("what is the cathegory of the item bought ? ").capitalize()

    #saving collected inputs as instance of expenses class
        return cls(item,amount,category,date)
    
    def add_expenses(self):
        all_Expenses.append([self.item,self.amount, self.date,self.category])      
    
    def get_expense_by_category(self):
        if self.category not in all_categories.keys():
            all_categories[self.category] = [] #creating an empty item object

        all_categories[self.category].append({  #assignning object values
                "Item Name":self.item,
                "Amount":self.amount, 
                "Date":self.date })
        # for key, value in all_categories.items():
        #     print(f"{key} : {value["Item Name"]}\n")

