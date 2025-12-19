import json

def add_contact(contacts):
    print("\n=== ADD NEW CONTACT ===")
    name = input("Enter name: ")
    mobile_no = input("Enter mobile number: ")
    
    new_contact = {
        "name": name,
        "mobileNumber": mobile_no
    }
    
    contacts.append(new_contact)
    save_contact(contacts)
    print(f"✅ {name} added to contacts!")

def view_all_contact(contacts):
    if not contacts:
        print("\n📱 No Contacts Yet!")
        return
    
    print("\n=== YOUR CONTACTS ===")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']}")
        print(f"   📞 {contact['mobileNumber']}")
    print("=" * 25)

def delete_contact(contacts):
    if not contacts:
        print("\n📱 No contacts to delete!")
        return
    
    view_all_contact(contacts)
    
    try:
        del_contact = input("\nEnter contact number to delete: ")
        index = int(del_contact) - 1
        
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contact(contacts)
            print(f"🗑️ Deleted: {deleted['name']}")
        else:
            print("❌ Invalid contact number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def save_contact(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def load_contact():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    contacts = load_contact()
    
    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Choose 1-4")

if __name__ == "__main__":
    main()