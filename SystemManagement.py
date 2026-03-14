class menu:
    def show (self):
        print("\n===== FOOTBALL FIELD MANAGEMENT =====")
        print("1.Field_management")
        print("2.Booking_management")
        print("3.Customer_management")
        print("4.Revenue_management")
        print("Exit")

    def process (self):
        field = Field_management()
        book = Booking_management()
        customer = Customer_management()
        revenue = Revenue_management()

        self.show()
        choice = input("Enter your choice:")

        if choice == 1:
            field.menu()
        if choice == 2:
            book.menu()
        if choice == 3:
            customer.menu()
        if choice == 4:
            revenue.menu()

def main():
    menu = menu()
    menu.show()
    menu.process()


if __name__ == "__main__":
    main()