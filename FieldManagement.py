from data import FieldRecord, save_field_to_file, load_field_from_file

class FieldManagement:
    def __init__(self):
        self.fields = load_field_from_file()

    # từ object sang string
    def save_fields(self):
        save_field_to_file(self.fields)

    # tạo ID tự động
    def generate_field_id(self):
    # 1. Handle empty list immediately
        if not self.fields:
            return "F0001"

        def parse_id_safely(field_obj):
            """Helper to extract (Prefix, NumericValue) from an ID string."""
            f_id = str(field_obj.field_id).strip()
            if not f_id:
                return ("F", 0)
            
            try:
                prefix = f_id[0]
                # Try to grab everything after the first character as an int
                number = int(f_id[1:])
                return (prefix, number)
            except (ValueError, IndexError):
                # If it's just "F" or "F-abc", treat number as 0 so it doesn't crash max()
                return (f_id[0] if f_id else "F", 0)

        try:
            # 2. Find the record with the highest ID based on our safe parser
            last_record = max(self.fields, key=parse_id_safely)
            letter, last_number = parse_id_safely(last_record)
            
            # 3. Increment and format with 4-digit padding
            return f"{letter}{last_number + 1:04d}"

        except Exception:
            # 4. Final safety net: if max() fails for any reason, 
            # use the count of fields to create a unique ID.
            return f"F{len(self.fields) + 1:04d}"
        
    # thêm sân
    def add_field(self):
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
        new_field = FieldRecord(field_id, field_name, field_type, float(field_cost), "Active")
        self.fields.append(new_field)
        self.save_fields()
        print("Save Succesfully")

    # xem sân
    def view_field_list(self):
        if not self.fields:
            print("No Field")
            return
        # format cho đẹp
        print("{:<10}{:<12}{:<10}{:<10}{:<12}".format(
            "ID",
            "Name",
            "Type",
            "Cost",
            "Status"
        ))
        print("-" * 55)
        for f in self.fields:
            print(f)

    # lọc sân cho ra kết quả
    def filter_field(self):
        print("\nEnter filter (0 = show all)")
        field_id = input("Field ID: ").strip()
        field_name = input("Field Name: ").strip().lower()
        field_type = input("Field Type: ").strip()
        # những kế quả phù hợp sẽ nằm ở results
        results = []
        # thêm điềm kiện, 0 thì lấy hết
        for f in self.fields:
            if field_id != "0" and field_id != f.field_id:
                continue
            if field_name != "0" and field_name not in f.field_name.lower():
                continue
            if field_type != "0" and field_type != f.field_type:
                continue
            results.append(f)
        if not results:
            print("No result found")
            return
        # format cho đẹp
        print("{:<10}{:<12}{:<10}{:<10}{:<12}".format(
            "ID",
            "Name",
            "Type",
            "Cost",
            "Status"
        ))
        print("-" * 55)
        for f in self.fields:
            print(f)

    def edit_field(self):
        if not self.fields:
            print("No fields found.")
            return
        field_id = input("Enter Field ID to edit: ").strip()
        for c in self.fields:
            if c.field_id == field_id :
                print("Leave blank to keep current value.")
                new_name = input(f"New Name ({c.field_name}): ").strip()

                print("Leave blank to keep current value.")
                new_type = input(f"New Type ({c.field_type}): ").strip()

                if new_name:
                    c.field_name = new_name
                if new_type:
                    c.new_type = new_type

                self.save_fields()
                print("Field updated successfully!")
                return   
    # xoá sân
    def del_field(self):
        field_id = input("Enter Field ID to delete: ").strip()
        for f in self.fields:
            if f.field_id == field_id:
                if f.status == "inactive":
                    print("Field already inactive")
                    return
                f.status = "inactive"
                self.save_fields()
                print("Field set to inactive")
                return
        print("Field not found")
    def check_field_active(self, field_id):
        for f in self.fields:
            if f.field_id == field_id:
                if f.field_status.lower() == "active":
                    return True
                else:
                    print("Field is inactive")
                    return False
        print("Field not found/inactive")
        return False
    
    def field_cost(self, field_id):
        for f in self.fields:
            if f.field_id == field_id:
                return f.field_cost
        return None
    
    # giao diện chính
    def menu(self):
      while True:
        print("\n===== FIELD MANAGEMENT =====")
        print("1. Add Field")
        print("2. View Fields List")
        print("3. Edit Field")
        print("4. Filter Fields")
        print("5. Delete Fields")
        print("0. <<<Back")
        choice = input("Choose: ").strip()

        # các lựa chọn
        if choice == "1":
            self.add_field()
        elif choice == "2":
            self.view_field_list()
        elif choice =="3":
            self.edit_field()
        elif choice =="4":
            self.filter_field()
        elif choice =="5":
            self.del_field()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    manager = FieldManagement()
    manager.menu()
