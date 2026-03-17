class Customer:
    def __init__(self, customer_id, customer_name, number, status = "active"):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.number = number
        self.status = status
    def to_string(self):
        return f"{self.customer_id},{self.customer_name},{self.number},{self.status}"

    @staticmethod
    def from_string(data):
        parts = data.strip().split(",")
        return Customer(
            parts[0],
            parts[1],
            parts[2],
            parts[3] if len(parts) > 3 else "active"#nếu ai chưa set status thì tự set thành active
        )


    def display(self):
        print(f"{self.customer_id:<10}{self.customer_name:<20}{self.number:<15}{self.status:<10}")
from data import load_customer_from_file, save_customer_to_file, CustomerRecord 
import os
class CustomerManager:
    def __init__(self):
        self.customer= []
        self.customer_file = "customer.txt"
        self.load_customers()

    def load_customers(self):
        records = load_customer_from_file()

        self.customer = []

        for r in records:
            c = Customer(r.customer_id, r.name, r.phone, r.status)
            self.customer.append(c)
    def save_customer(self):

        records = []

        for c in self.customer:
            records.append(CustomerRecord(
                c.customer_id,
                c.customer_name,
                c.number,
                c.status
            ))

        save_customer_to_file(records)
    def generate_customer_id(self):
        if not self.customer:
            return "A0001"

        last = max(self.customer, key=lambda c: (c.customer_id[0], int(c.customer_id[1:])))#so số lớn nhất để + lên thành ID t2
        last_id = last.customer_id

        letter = last_id[0]
        number = int(last_id[1:]) + 1
        return f"{letter}{number:04d}"
    def addCustomer(self):
        print("\n=== Add Customer ===")
        
        customer_id = self.generate_customer_id()
        print("Customer ID:", customer_id)

        customer_name = input("Enter Customer Name: ").strip()
        number = input("Please Enter your Phone NUmber:")
        if not number.isdigit():
            print("Phone only contain digits")
            return
        if not customer_name or not number:
            print("Missing Information")
            return

        new_customer= Customer(customer_id, customer_name, number)
        self.customer.append(new_customer)
        self.save_customer()
        print("Save Succesfully")
    def displayCustomer(self):
        if not self.customer:
            print("No Customer")
            return
        print("\nID        Name               Phone           Status   ")
        print("-" * 60)
        for c in self.customer:
            c.display()
    def editCustomer(self):
        if not self.customer:
            print("No customers found.")
            return
        customer_id = input("Enter Customer ID to edit: ").strip()
        for c in self.customer:
            if c.customer_id == customer_id:
                print("Leave blank to keep current value.\n")

                new_name = input(f"New Name ({c.customer_name}): ").strip()
                new_number = input(f"New Phone ({c.number}): ").strip()

                if new_name:
                    c.customer_name = new_name
                if new_number:
                    if new_number.isdigit():
                        c.number = new_number
                    else:
                        print("Invalid phone number. Keeping old phone.")

                self.save_customer()
                print("Customer updated successfully!")
                return   
    def filterCustomer(self):
        print("\nEnter filter (0 = show all)")

        customer_id = input("Customer ID: ").strip()
        customer_name = input("Name: ").strip().lower()
        number = input("Phone: ").strip()

        results = []

        for c in self.customer:

            if customer_id == "0" and customer_name == "0" and number == "0":
                results.append(c)
                continue

            if customer_id and customer_id != "0" and customer_id == c.customer_id:
                results.append(c)

            elif customer_name and customer_name != "0" and customer_name in c.customer_name.lower():
                results.append(c)

            elif number and number != "0" and number == c.number:
                results.append(c)

        if not results:
            print("No result found")
            return

        print("\nID        Name                Phone          Status")
        print("-" * 60)

        for c in results:
            c.display()
    def deleteCustomer(self):
        customer_id = input("Enter Customer ID to delete: ").strip()

        for c in self.customer:
            if c.customer_id == customer_id:

                if c.status == "inactive":
                    print("Customer already inactive")
                    return

                c.status = "inactive"
                self.save_customer()

                print("Customer set to inactive")
                return

        print("Customer not found")
    def findCustomer(self):
        if not self.customer:
            print("No customer found:")
            return
        customer_name_input = input("Enter Customer Name: ").strip().lower()
        number_input = input("Enter Phone Number: ").strip()

        results = [
            c for c in self.customer
            if customer_name_input in c.customer_name.lower() and number_input == c.number
        ]
        if not results:
            print("No matching customer found.")
            return 
        print("\nID        Name                     Phone            Status    ")
        print("-" * 75)
        for c in results:
            c.display()
    def check_customer_active(self, customer_id):

        for c in self.customer:
    
            if c.customer_id == customer_id:

                if c.status == "active":
                    return True
                else:
                    print("Customer is inactive")
                    return False

        print("Customer not found")
        return False
        
def main():
    manager = CustomerManager()

    while True:
        print("\n===== CUSTOMER MANAGEMENT =====")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Edit Customer")
        print("4. Find Customer")
        print("5 Filter Customer")
        print("6 Delete Customer")
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
        elif choice =="5":
            manager.filterCustomer()
        elif choice =="6":
            manager.deleteCustomer()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
