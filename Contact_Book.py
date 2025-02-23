contacts = {}

while True:
    print("\nContact Book")
    print("1. Create contact")
    print("2. View all")
    print("3. View one contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Search contact")
    print("7. Count contact")
    print("8. Exit\n")

    choice = input("Enter your choice = ")

    if choice == "1":
        name = input("Enter your name = ")
        if name in contacts:
            print(f'Contact name {name} already exits!\n')
        else:
            email = input("Enter email = ")
            mobile = input("Enter your mobile = ")
            address = input("Enter your address = ")
            contacts[name] = {'name': name, 'email': email, 'mobile': mobile, 'address': address}
            print(f"Contact name {name} has been created successfully!\n")

    elif choice == "2":
        if contacts:
            print("\nAll Contacts:")
            for name, contact in contacts.items():
                print(f"Name: {name}, Mobile: {contact['mobile']}, Email: {contact['email']}, Address: {contact['address']}")
            print()
        else:
            print("No contacts available!\n")

    elif choice == "3":
        name = input("Enter contact name to view = ")     
        if name in contacts:
            contact = contacts[name] 
            print(f"Name: {contact['name']}, Mobile: {contact['mobile']}, Email: {contact['email']} , Address: {contact['address']}\n")
        else:
            print("Contact not found!\n")
    
    elif choice == "4":
        name = input("Enter name to update contact = ")
        if name in contacts:
            email = input("Enter email = ")
            mobile = input("Enter your mobile = ")
            address = input("Enter your address = ")
            contacts[name] = {'name': name, 'email': email, 'mobile': mobile, 'address': address}
            print(f"Contact name {name} has been updated successfully!\n")
        else:
            print("Contact not found!\n")
    
    elif choice == "5":
        name = input("Enter contact name to delete = ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} is deleted successfully!\n")
        else:
            print("Contact not found!\n")
    
    elif choice == "6":
        search_name = input("Enter contact name to search = ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found - Name: {name}, Mobile Number: {contact['mobile']}, Email: {contact['email']}, Address: {contact['address']}\n")
                found = True
        if not found:
            print("No contact found with that name\n")

    elif choice == "7":
        print(f"Total contacts in your book : {len(contacts)}\n")

    elif choice == "8":
        print("Closing this contact book!\n")
        break

    else:
        print("Invalid input!\n")