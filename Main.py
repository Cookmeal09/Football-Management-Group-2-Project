from SystemManager import SystemManager
print("Program started")
def menu():
    print("\n====== FIELD MANAGEMENT ======")
    print("1. Add Field")
    print("2. Display Fields")
    print("3. Find Field")
    print("4. Edit Field")
    print("5. Update Status")
    print("0. Exit")

def main():
    manager = SystemManager()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            manager.add_field()
        elif choice == "2":
            manager.display_fields()
        elif choice == "3":
            manager.find_field()
        elif choice == "4":
            manager.edit_field()
        elif choice == "5":
            manager.update_status()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()