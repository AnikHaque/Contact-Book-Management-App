from contact_manager import ContactManager
from file_handler import load_from_file, save_to_file

FILENAME = "contacts.csv"

def print_menu():
    print("\n=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")

def print_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    print("\n===== All Contacts =====")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name : {contact['name']}")
        print(f"   Phone : {contact['phone']}")
        print(f"   Email : {contact['email']}")
        print(f"   Address: {contact['address']}")
    print("========================")

def main():
    manager = ContactManager()
    data = load_from_file(FILENAME)
    manager.load_contacts(data)

    print("Welcome to the Contact Book CLI System!")
    print(f"Loading contacts from {FILENAME}... Done!")

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")

            from utils import is_valid_name, is_valid_phone, is_valid_email

            if not is_valid_name(name):
                print("Error: The contact’s name must be a string.")
                continue
            if not is_valid_phone(phone):
                print("Error: The phone number must be an 11-digit number.")
                continue
            if not is_valid_email(email):
                print("Error: Invalid email format.")
                continue

            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            success, message = manager.add_contact(contact)
            print(message)
            if success:
                save_to_file(FILENAME, manager.get_contacts())

        elif choice == "2":
            print_contacts(manager.get_contacts())

        elif choice == "3":
            term = input("Enter search term (name/email/phone): ")
            result = manager.search_contacts(term)
            if result:
                print_contacts(result)
            else:
                print("No contact found.")

        elif choice == "4":
            phone = input("Enter the phone number of the contact to delete: ")
            confirm = input(f"Are you sure you want to delete contact number {phone}? (y/n): ")
            if confirm.lower() == 'y':
                success = manager.remove_contact(phone)
                if success:
                    save_to_file(FILENAME, manager.get_contacts())
                    print("Contact deleted successfully!")
                else:
                    print("Contact not found.")
            else:
                print("Deletion cancelled.")

        elif choice == "5":
            print("Thank you for using the Contact Book CLI System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
