contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact {name} added.")
    
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
            
def main():
    while True:
        print("\n***Contact Manager***")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    
with open("contacts.txt", "w") as file:
    for name, phone in contacts.items():
        file.write(f"{name},{phone}\n")