from Field import Field
import os

class SystemManager:
    def __init__(self):
        self.fields = []
        self.filename = "fields.txt"
        self.load_file()

    # =========================
    # LOAD FILE
    # =========================
    def load_file(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    self.fields.append(Field.from_string(line))
        except:
            print("Error reading file.")

    # =========================
    # SAVE FILE
    # =========================
    def save_file(self):
        try:
            with open(self.filename, "w") as f:
                for field in self.fields:
                    f.write(field.to_string() + "\n")
        except:
            print("Error writing file.")

    # =========================
    # VALIDATE STATUS (DÙNG CHUNG)
    # =========================
    def choose_status(self):
        while True:
            print("Choose status:")
            print("1. Available")
            print("2. Maintenance")
            print("3. Inactive")

            choice = input("Enter choice (1-3): ")

            status_dict = {
                "1": "Available",
                "2": "Maintenance",
                "3": "Inactive"
            }

            if choice in status_dict:
                return status_dict[choice]
            else:
                print("Invalid choice! Try again.\n")

    # =========================
    # ADD FIELD
    # =========================
    def add_field(self):
        field_id = input("Enter Field ID: ")

        for field in self.fields:
            if field.field_id == field_id:
                print("ID already exists!")
                return

        name = input("Enter Name: ")

        # VALIDATE TYPE
        while True:
            field_type = input("Enter Type (5/7): ")
            if field_type in ["5", "7"]:
                break
            print("Type must be 5 or 7!")

        # VALIDATE COST
        while True:
            try:
                cost = float(input("Enter Cost per hour: "))
                if cost >= 1000:
                    break
                else:
                    print("Cost must be at least 1000!")
            except:
                print("Invalid cost!")

        status = "Available"
        is_booking = False  # mặc định chưa đặt

        new_field = Field(field_id, name, field_type, cost, status, is_booking)
        self.fields.append(new_field)
        self.save_file()
        print("Field added successfully!")

    # =========================
    # DISPLAY
    # =========================
    def display_fields(self):
        if not self.fields:
            print("No fields available.")
            return

        print(f"{'ID':<10}{'Name':<15}{'Type':<10}{'Cost':<15}{'Status':<15}{'Booking':<10}")
        print("-" * 75)
        for field in self.fields:
            field.display()

    # =========================
    # FIND
    # =========================
    def find_field(self):
        search_id = input("Enter Field ID to search: ")
        for field in self.fields:
            if field.field_id == search_id:
                field.display()
                return
        print("Field not found.")

    # =========================
    # EDIT FIELD
    # =========================
    def edit_field(self):
        edit_id = input("Enter Field ID to edit: ")

        for field in self.fields:
            if field.field_id == edit_id:

                field.name = input("New Name: ")

                # VALIDATE TYPE
                while True:
                    new_type = input("New Type (5/7): ")
                    if new_type in ["5", "7"]:
                        field.field_type = new_type
                        break
                    print("Type must be 5 or 7!")

                # VALIDATE COST
                while True:
                    try:
                        new_cost = float(input("New Cost: "))
                        if new_cost >= 1000:
                            field.cost = new_cost
                            break
                        else:
                            print("Cost must be at least 1000!")
                    except:
                        print("Invalid cost.")

                # CHOOSE STATUS
                field.status = self.choose_status()

                self.save_file()
                print("Field updated successfully!")
                return

        print("Field not found.")

    # =========================
    # UPDATE STATUS
    # =========================
    def update_status(self):
        edit_id = input("Enter Field ID: ")

        for field in self.fields:
            if field.field_id == edit_id:

                field.status = self.choose_status()
                self.save_file()
                print("Status updated!")
                return

        print("Field not found.")