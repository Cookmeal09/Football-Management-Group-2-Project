class Field:
    def __init__(self,field_id, field_name, field_status, field_type, field_cost):
        self.field_id = field_id
        self.field_name = field_name
        self.field_type = field_type
        self.field_cost = field_cost
        self.field_status = field_status
    def to_string(self):
      return f"{self.field_id},{self.field_name},{self.field_type},{self.field_cost},{self.field_status}"
    @staticmethod
    def from_string(self):
      part = data.strip().split(",")
      return Booking(
          part[0],
          part[1],
          part[2],
          float(part[3]),
          part[4] if len(parts) > 3 else "active"
    )
    def display(self):
      print("{:<10}{:<12}{:<10}{:<10}{:<12}".format(
        self.field_id,
        self.field_name,
        self.field_type,
        self.field_cost,
        self.field_status
    ))
class FieldManagement():
    def __init__(self):
        self.fields = []
        self.field_file = "field.txt"
        self.load_field()
    def load_field(self):
        if not os.path.exists(self.field_file):
            return
        with open(self.field_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == "":
                continue
            try:
                self.fields.append(Field.from_string(line))
            except:
                continue
    def save_field(self):
        with open(self.field_file, "w", encoding="utf-8") as f:
            for i in self.fields:
                f.write(i.to_string() + "\n")
    def generate_field_id(self):
        if not self.fields:
            return "F0001"
        last = max(self.fields, key=lambda f: (f.field_id[0], int(f.field_id[1:])))
        last_id = last.field_id
        letter = last_id[0]
        number = int(last_id[1:]) + 1
        return f"{letter}{number:04d}"
    def add_customer(self):
        print("\n=== Add Field ===")
        field_id = self.generate_field_id()
        print("Field ID:", field_id)
        field_name = input("Enter Field Name: ").strip()
        field_type = input("Enter Field Type: (number of players in a field) ").strip()
        field_cost = input("Enter Field Cost: ").strip()

        # kiểm tra hợp lệ
        if not field_name or not field_type or not field_cost:
            print("Missing information, please try again")
            return
        if not field_type.isdigit():
            print("Field type should only contain digits")
            return
        if not field_cost.isdigit():
            print("Field cost should only contain digits")
            return
        if len(field_cost) <= 3:
            field_cost *= 1000
        else:
            print("Invalid input")

        # Tạo object
        new_field = Field(field_id, field_name, field_type, field_cost)
        self.field.append(new_field)
        self.save_field()
        print("Save Succesfully")
    def view_field_list(self):
        if not self.field:
            print("No Field")
            return
        print("{:<10}{:<12}{:<10}{:<10}{:<12}".format(
            "ID",
            "Name",
            "Type",
            "Cost",
            "Status"
        ))
        print("-" * 55)
        for f in self.field:
            f.display()


    def filter_field(self):
        print("\nEnter filter (0 = show all)")

        field_id = input("Field ID: ").strip()
        field_name = input("Field Name: ").strip().lower()
        field_type = input("Field Type: ").strip()

        results = []

        for f in self.field:
            if field_id != "0" and field_id != f.field_id:
                continue
            if field_name != "0" and field_name not in f.field_name.lower():
                continue
            if field_type != "0" and field_type != f.field_type:
                continue
            results.append(c)
        if not results:
            print("No result found")
            return
        print("{:<10}{:<12}{:<10}{:<10}{:<12}".format(
            "ID",
            "Name",
            "Type",
            "Cost",
            "Status"
        ))
        print("-" * 55)
        for f in self.field:
            f.display()
    def del_field(self):
        field_id = input("Enter Field ID to delete: ").strip()
        for f in self.field:
            if f.field_id == field_id:
                if f.status == "inactive":
                    print("Field already inactive")
                    return
                f.status = "inactive"
                self.save_field()
                print("Field set to inactive")
                return
        print("Field not found")
    def main():
      manager = FieldManagement()
      while True:
        print("\n===== FIELD MANAGEMENT =====")
        print("1. Add Field")
        print("2. View Fields List")
        print("3. Edit Field")
        print("4. Filter Fields")
        print("5. Delete Fields")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            manager.add_field()
        elif choice == "2":
            manager.view_field_list()
        elif choice =="3":
            manager.edit_customer()
        elif choice =="4":
            manager.filter_field()
        elif choice =="6":
            manager.del_field()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
