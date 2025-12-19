import json

def add_contact(contacts):
    print("\n=== ADD NEW CONTACT ===")
    name = input("Enter name: ").lower()
    mobile_no = input("Enter mobile number: ")

    if not mobile_no.isdigit():
        print("❌ Error: Mobile number must contain only digits!")
        return
    
    for contact in contacts:
        if contact['mobileNumber'] == mobile_no:
            print(f"❌ Error: This mobile number already belongs to {contact['name']}!")
            return
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
        print("\n📱 Database is Empty!")
        return
    
    view_all_contact(contacts)
    
    try:
        del_contact = input("\nEnter serial contact number to delete: ")
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
    except json.JSONDecodeError:
        print("⚠️ Warning: contacts.json is corrupted! Starting with an empty list.")
        return []
    
def search_contact(contacts):
    if not contacts:
        print("\n📱 Database is Empty!")
        return
    
    query = input("Enter The Name you want to Search for: ").lower()

    found = False
    print("\n=== SEARCH RESULTS ===")
    for contact in contacts:
        if query in contact['name']:
            print(f"✅ Found: {contact['name']} | 📞 {contact['mobileNumber']}")
            found = True
            
    if not found:
        print(f"❌ No contact found matching '{query}'")
    

def main():
    contacts = load_contact()
    
    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Delete Contact")
        print("4. Search")
        print("5. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            print("GoodBye!")
            break
        else:
            print("❌ Invalid choice! Choose 1-4")

if __name__ == "__main__":
    main()
