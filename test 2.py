# initialize an empty dictionary to store phone records
phone_directory = {}

# define the main menu function
def menu():
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU")
    print("Menu")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")

    # ask for user input
    choice = input("Enter your choice: ")

    # process user input
    if choice == "1":
        add_record()
    elif choice == "2":
        search_record()
    elif choice == "3":
        change_record()
    elif choice == "4":
        delete_record()
    elif choice == "5":
        quit_program()
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
        menu()

# define function to add a new phone record
def add_record():
    name = input("Enter name: ")
    phone_number = input("Enter your 10-digit phone number: ")
    phone_directory[name] = phone_number
    print("Record added\n")
    menu()

# define function to search for a phone record
def search_record():
    name = input("Enter name to search: ")
    if name in phone_directory:
        print(f"{name}: {phone_directory[name]} ")
    else:
        print(f"No record found for {name}\n")
    menu()

# define function to change an existing phone number
def change_record():
    name = input("Enter name: ")
    if name in phone_directory:
        phone_number = input("Enter new 10-digit phone number: ")
        phone_directory[name] = phone_number
        print("Record updated\n")
    else:
        print(f"No record found for {name}\n")
    menu()

# define function to delete an existing phone record
def delete_record():
    name = input("Enter name: ")
    if name in phone_directory:
        del phone_directory[name]
        print("Record deleted\n")
    else:
        print(f"No record found for {name}\n")
    menu()

# define function to quit the program
def quit_program():
    print("Goodbye!")
    exit()

# start the program by calling the menu function
menu()
