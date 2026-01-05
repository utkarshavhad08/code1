contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    print("Contact added successfully\n")

def view_contacts():
    if not contacts:
        print("No contacts available\n")
        return

    for i, contact in enumerate(contacts, start=1):
        print(i, contact["name"], contact["phone"], contact["email"])
    print()

def search_contact():
    search_name = input("Enter name to search: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print("Name :", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found\n")
    else:
        print()

def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully\n")
            return

    print("Contact not found\n")

while True:
    print("Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book")
        break
    else:
        print("Invalid choice\n")