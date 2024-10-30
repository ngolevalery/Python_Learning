import csv

contact_list = {}

name_pairs = {
    'Alice': 'Bob',
    'Charlie': 'Daisy',
    'Eve': 'Frank',
    'George': 'Hannah',
    'Ivy': 'Jack'
}

# Write dictionary to CSV file
# def save_dict_to_csv(filename, data):
#     # Open the file in write mode initially to create headers
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         # Write header
#         writer.writerow(['Name1', 'Name2'])
#         # Write each key-value pair as a new row
#         for name1, name2 in data.items():
#             writer.writerow([name1, name2])

# # Save the name_pairs dictionary to CSV
# save_dict_to_csv('names.csv', name_pairs)


#functions to write to csv.
def update_csv(csv_filename,contact_list):
     with open("contactlist.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Phone Number'])
        for name, phoneNumber in contact_list.items():
            writer.writerow([name,phoneNumber])

print("contact list file has been updated")


# FUNCTION TO ADD CONTACTS
def add_contact(contact_name="x", phone_number="y"):
    contact_name = input("\nEnter Contact Name: ").capitalize()
    phone_number = input("Enter Phone Number:  ")
    contact_list.update({contact_name: phone_number})
    update_csv("contactlist.csv",contact_list)
    return contact_list



# FUNCTION TO VIEW ALL CONTACTS
def view_contacts():
    print("----------Your Contacts---------")
    print("NAME        PHONE NUMBER")
    for key,value in contact_list.items():
        print("---------------------------")
        print(f"{key}:{value}")


# FUNCTION TO EDIT CONTACTS
def edit_contact(name="x"):
    name = input("Please enter the name of the contact you want to edit: ").capitalize()
    if name in contact_list:
        print(contact_list[name])
    else:
        print("could not find name")
        return
    action_control = input(
        "Are you sure you want to edit this contact? Enter y or n "
    ).lower()
    if action_control == "y":
        new_number = input(f"enter {name}'s new number: ")
        contact_list.update[name]= new_number
        print(f"{name}'s phone number has been updated to {contact_list[name]}")
        update_csv("contactlist.csv",contact_list)
    elif action_control == "n":
        print("Action Cancelled !")
    else:
        print("invalid input! Could not complete action")
        return


# FUNCTION TO DELETE CONTACTS
def delete_contact(name="x"):
    name = input("Enter the name of the contact you want to delete: ").capitalize()
    if name in contact_list:
        action_control = input(
            f"Are you sure you want to delete {name}'s contact ? y/n: "
        ).lower()
        if action_control == "y":
            contact_list.remove(name)
            print("\nContact successfully deleted")
            update_csv("contactlist.csv",contact_list)
        elif action_control == "n":
            print("action cancelled")
            return
        else:
            print("invalid option")
            return
    else:
        print("contact not found !")
        return
