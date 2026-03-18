from FieldManagement import FieldManagement
from BookingManagement import BookingManagement
from CustomerManagement import CustomerManagement
from PaymentManagement import PaymentManagement
class Menu:

    def show(self):
        print("\n===== MINI FOOTBALL FIELD MANAGEMENT =====")
        print("1. Field_management")
        print("2. Booking_management")
        print("3. Customer_management")
        print("4. Revenue_management")
        print("0. Exit")

    def process(self):
        field = FieldManagement()
        book = BookingManagement()
        customer = CustomerManagement()
        payment = PaymentManagement()

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
                payment.menu()

            elif choice == "0":
                print("Exiting program...")
                break

            else:
                print("Invalid choice!")


def main():
    menu = Menu()
    menu.process()


if __name__ == "__main__":
    main()