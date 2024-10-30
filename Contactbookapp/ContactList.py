import allfunctions as allf
import time

print("----------CONTACT LIST----------")

print("Please select an option to continue...\n")

contact_app_open = True

while contact_app_open:
    print("Enter 1 to Add a new contact...\n")
    print("Enter 2 to View all contacts...\n")
    print("Enter 3 to Edit a contact...\n")
    print("Enter 4 to Delete a contact...\n")
    print("Enter 0 to Exit program ...\n")

    #taking input from user
    action = input("What do you want to do? ")

    #a list of all action choices
    options = ["0","1","2","3","4"]

    #checkin user input to perform required action

    if action not in (options):
        print("\nInvalid option !!!")
        action = input("Enter again: ") 

    if action == "1":
        allf.add_contact() #calling the add_contacts function
        print("Contact was successfully added !")
    elif action == "2":
        allf.view_contacts() #calling the view_contact function
    elif action == "3":
        allf.edit_contact() #calling the edit_contact function
    elif action == "4":
        allf.delete_contact() #Delete contact fxn
    elif action == "0":
        print("exiting...")
        time.sleep(2)
        contact_app_open = False


    print("--------------------")
