
# Session Date: December 2, 2025

## **What I Built**
- Working contact manager with menu system
- Add contacts, view contacts, exit functionality

## **What I Debugged**
- Fixed infinite loop caused by `contacts = {}` inside loop
- Understood variable scope (global vs local)

## **What I Learned**
- `if __name__ == "__main__"` pattern and why it matters
- File persistence concept (save/load from disk)
- Menu-driven programs with while loops

## **Time Invested**
- 45 minutes (limited due to late work shift)

## **How I Feel**
- Confident: 7/10
- Understood the debugging process
- Ready for weekend enhancements



Code: 

```cpp title:contactmanager.py

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

            save_contacts()

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

```
```

