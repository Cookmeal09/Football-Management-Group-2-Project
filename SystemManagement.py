class Menu:

    def show(self):
        print("\n===== FOOTBALL FIELD MANAGEMENT =====")
        print("1. Field_management")
        print("2. Booking_management")
        print("3. Customer_management")
        print("4. Revenue_management")
        print("5. Exit")

    def process(self):
        field = Field_management()
        book = Booking_management()
        customer = Customer_management()
        revenue = Revenue_management()

        while True:
            self.show()
            choice = input("Enter your choice: ")

            if choice == "1":
                field.menu()

            elif choice == "2":
                book.menu()

            elif choice == "3":
                customer.menu()

            elif choice == "4":
                revenue.menu()

            elif choice == "5":
                print("Exiting program...")
                break

            else:
                print("Invalid choice!")


def main():
    menu = Menu()
    menu.process()


if __name__ == "__main__":
    main()