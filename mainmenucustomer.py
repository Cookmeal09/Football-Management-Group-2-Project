from CustomerManager import CustomerManager
def main():
    manager = CustomerManager()

    while True:
        print("\n===== CUSTOMER MANAGEMENT =====")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Edit Customer")
        print("4. Find Customer")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            manager.addCustomer()
        elif choice == "2":
            manager.displayCustomer()
        elif choice =="3":
            manager.editCustomer()
        elif choice =="4":
            manager.findCustomer()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()