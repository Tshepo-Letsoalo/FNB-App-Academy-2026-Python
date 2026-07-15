contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added!")

def search_contact():
    name = input("Enter name to search: ")
    for c in contacts:
        if c["name"] == name:
            print(f"Found: {c}")
            return
    print("Not found.")

def delete_contact():
    name = input("Name to delete: ")
    for c in contacts:
        if c["name"] == name:
            contacts.remove(c)
            print("Deleted.")
            return
    print("Contact not found.")

def view_all():
    for c in contacts:
        print(f"{c['name']} | {c['phone']} | {c['email']}")

while True:
    print("\n1.Add 2.Search 3.Delete 4.View 5.Exit")
    choice = input("Choose: ")
    if choice == '1': add_contact()
    elif choice == '2': search_contact()
    elif choice == '3': delete_contact()
    elif choice == '4': view_all()
    elif choice == '5': break