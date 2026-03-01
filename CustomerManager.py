from Field import Field
from customer import Customer
import os
class CustomerManager:
    def __init__(self):
        self.customer= []
        self.customer_file = "customer.txt"
        self.load_customers()
        self.field_file = "field.txt"

    def load_customers(self):
        if not os.path.exists(self.customer_file):
            return
        with open(self.customer_file, "r", encoding="utf-8") as f:#mở file customer.txt để đọc r đóng file lại
            for line in f:
                self.customer.append(Customer.from_string(line))
    def save_customer(self):
        with open(self.customer_file,"w", encoding="utf-8") as f:
            for c in self.customer:
                f.write(c.to_string() + "\n")
    def load_fields(self):
        fields = []
        if not os.path.exists(self.field_file):
            return fields
        with open(self.field_file, "r", encoding="utf-8") as f:
            for line in f:
                field = Field.from_string(line)
                fields.append(field)
        return fields
    def choose_field(self, field_type_input):
        fields =self.load_fields()#show hết các field
        if not fields:
            print("No fields available")
            return None
        print("\n=== Available Fields ===")#chỉ là chỉnh sửa các vị trí thông tin của fields
        print(f"{'Field ID':<10} {'Field Name':<12} {'Price':<10}")
        print("="*30)
        available_ids = []#danh sách các field available và chưa ai đặt
        for field in fields:
            if field.status=="Available" and field.field_type==field_type_input and not field.is_booking:
                print(f"{field.field_id:<10}{field.field_type + ' players':<12}{field.cost:<10}")
                available_ids.append(field.field_id)
        if not available_ids:
            print("No available fields at the moment.")
            return None
        while True:
            selected_id = input("Enter Field ID to book: ").strip()
            if selected_id not in available_ids:
                print("No field in the list, please enter field again.")
                continue
            return selected_id
    def addCustomer(self):
        print("\n=== Add Customer ===")
        while True:
            customer_id = int(input("Enter Customer ID(onlynumber): "))
            if not customer_id:
                print("Please enter Customer ID")
                continue
            if any(c.customer_id == customer_id for c in self.customer):
                print("Customer ID already exists")
                continue
            break
        name = input("Enter Customer Name: ").strip()
        phone = input("Please Enter your Phone NUmber:")
        if not phone.isdigit():
            print("Phone only contain digits")
            return
        booking_date = input("Enter Date Booking (DD-MM-YYYY)")
        booking_time = input("Enter Booking Time:").strip()
        if not name or not booking_time or not phone or not booking_date:
            print("Missing Information")
            return
        while True:
            field_type = input("Enter Field Type (5 or 7 players): ").strip()
            if field_type not in ["5", "7"]:
                print("Please enter 5 or 7 only.")
                continue
            break
        field_id=self.choose_field(field_type)
        if not field_id:
            return
        new_customer= Customer(customer_id, name, field_id, booking_time, booking_date, phone)#mới nên count =1 nên khỏi đặt
        self.customer.append(new_customer)
        self.save_customer()
        print("Save Succesfully")
    def displayCustomer(self):
        if not self.customer:
            print("No Customer")
            return
        
        print("\nSort by:")
        print("1. Name (A -> Z)")
        print("2. Booking Count (High -> Low)")

        choice = input("Choose: ").strip()

        if choice == "1":
            sorted_list = sorted(self.customer, key=lambda x: x.name.lower())#sắp xếp theo từ a-> key=lambda
        elif choice == "2":
            sorted_list = sorted(self.customer, key=lambda x: x.booking_count, reverse=True)#đảo ngược giảm dần
        else:
            print("Invalid choice.")
            return
        print("\nID        Name                Field ID  Time           Phone           Bookings")
        print("-" * 75)
        for c in sorted_list:
            c.display()
    def editCustomer(self):
        if not self.customer:
            print("No customers found.")
            return
        customer_id = int(input("Enter Customer ID to edit: ").strip())
        for c in self.customer:
            if c.customer_id == customer_id:
                print("Leave blank to keep current value.\n")

                new_name = input(f"New Name ({c.name}): ").strip()
                new_time = input(f"New Booking Time ({c.booking_time}): ").strip()
                new_phone = input(f"New Phone ({c.phone}): ").strip()

                if new_name:
                    c.name = new_name
                if new_time:
                    c.booking_time = new_time
                if new_phone:
                    if new_phone.isdigit():
                        c.phone = new_phone
                    else:
                        print("Invalid phone number. Keeping old phone.")

                self.save_customer()
                print("Customer updated successfully!")
                return   
    def findCustomer(self):
        if not self.customer:
            print("No customer found:")
            return
        name_input = input("Enter Customer Name: ").strip().lower()
        phone_input = input("Enter Phone Number: ").strip()

        results = [
            c for c in self.customer
            if name_input in c.name.lower() and phone_input == c.phone
        ]
        if not results:
            print("No matching customer found.")
            return

        print("\nID        Name                Field ID  Time           Phone           Bookings")
        print("-" * 75)
        for c in results:
            c.display()

        