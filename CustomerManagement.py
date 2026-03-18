from data import load_customer_from_file, save_customer_to_file, CustomerRecord 

def get_numeric_suffix(customer_id):
    """Safely extracts the number from 'C123' -> 123."""
    try:
        # We strip the first character and try to convert the rest
        return int(customer_id[1:])
    except (ValueError, TypeError, IndexError):
        # If it's not a number or the string is too short, return -1 
        # so it sorts to the bottom/beginning
        return -1
    
class CustomerManagement:
    def __init__(self):
        self.customers= load_customer_from_file()

    def save_customer(self):
        save_customer_to_file(self.customers)
    def generate_customer_id(self):
        if not self.customers:
            return "A0001"
        else:
            try:
                last = max(
                    self.customers, 
                    key=lambda c: (c.customer_id[0], get_numeric_suffix(c.customer_id))
                )
            except Exception as e:
                print(f"Sorting error: {e}")
                last = self.customers[-1] #so số lớn nhất để + lên thành ID t2
        last_id = last.customer_id

        letter = last_id[0]
        number = int(last_id[1:]) + 1
        return f"{letter}{number:04d}"
    def addCustomer(self):
        print("\n=== Add Customer ===")
        
        customer_id = self.generate_customer_id()
        print("Customer ID:", customer_id)

        customer_name = input("Enter Customer Name: ").strip()
        number = input("Please Enter your Phone Number:")
        if not number.isdigit():
            print("Phone only contain digits")
            return
        if not customer_name or not number:
            print("Missing Information")
            return

        new_customer= CustomerRecord(customer_id, customer_name, number)
        self.customers.append(new_customer)
        self.save_customer()
        print("Save Succesfully")
    def displayCustomer(self):
        if not self.customers:
            print("No Customer")
            return
        print("\nID        Name               Phone           Status   ")
        print("-" * 60)
        for c in self.customers:
            print(c)
    def editCustomer(self):
        if not self.customers:
            print("No customers found.")
            return
        customer_id = input("Enter Customer ID to edit: ").strip()
        for c in self.customers:
            if c.customer_id == customer_id:
                print("Leave blank to keep current value.\n")

                new_name = input(f"New Name ({c.customer_name}): ").strip()
                new_number = input(f"New Phone ({c.phone}): ").strip()

                if new_name:
                    c.customer_name = new_name
                if new_number:
                    if new_number.isdigit():
                        c.phone = new_number
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

        for c in self.customers:
            if customer_id == "0" and customer_name == "0" and number == "0":
                results.append(c)
                continue

            if customer_id and customer_id != "0" and customer_id == c.customer_id:
                results.append(c)

            elif customer_name and customer_name != "0" and customer_name in c.customer_name.lower():
                results.append(c)

            elif number and number != "0" and number == c.phone:
                results.append(c)

        if not results:
            print("No result found")
            return

        print("\nID        Name                Phone          Status")
        print("-" * 60)

        for c in results:
            print(c)
    def deleteCustomer(self):
        customer_id = input("Enter Customer ID to delete: ").strip()

        for c in self.customers:
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
        if not self.customers:
            print("No customers:")
            return
        customer_name_input = input("Enter Customer Name: ").strip().lower()
        number_input = input("Enter Phone Number: ").strip()
        results = [
            c for c in self.customers
            if customer_name_input in c.customer_name.lower() and number_input == c.phone
        ]
        if not results:
            print("No matching customer found.")
            return 
        print("\nID        Name                     Phone            Status    ")
        print("-" * 75)
        for c in results:
            print(c)
    def check_customer_active(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                if c.status == "active":
                    return True
                else:
                    print("Customer is inactive")
                    return False

        print("Customer not found")
        return False
    def listCustomer(self):
        return self.customers
    
    def get_customer(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None
    
    def menu(self):
        while True:
            print("\n===== CUSTOMER MANAGEMENT =====")
            print("1. Add Customer")
            print("2. Display Customers")
            print("3. Edit Customer")
            print("4. Find Customer")
            print("5. Filter Customer")
            print("6. Delete Customer")
            print("0. <<<Back")

            choice = input("Choose: ").strip()
            if choice == "1":
                self.addCustomer()
            elif choice == "2":
                self.displayCustomer()
            elif choice =="3":
                self.editCustomer()
            elif choice =="4":
                self.findCustomer()
            elif choice =="5":
                self.filterCustomer()
            elif choice =="6":
                self.deleteCustomer()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    CustomerManagement().menu()
