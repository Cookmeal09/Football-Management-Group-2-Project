from datetime import datetime
from CustomerManagement import CustomerManagement
from FieldManagement import FieldManagement
from data import load_booking_from_file, save_booking_to_file, BookingRecord

class BookingManagement:
    def __init__(self):
        self.bookings = load_booking_from_file()
        self.customer_manager=CustomerManagement()
        self.field_manager=FieldManagement()

    def save_booking(self):
        save_booking_to_file(self.bookings)
        
    def generate_booking_id(self):
        # 1. Handle Empty List Immediately
        if not self.bookings:
            return "B0001"

        def safe_parse_id(booking_obj):
            import re
            """Helper to extract (Letter, Number) even from messy IDs."""
            b_id = str(booking_obj.booking_id)
            # Use RegEx to find the first letter and all trailing digits
            match = re.match(r"([A-Za-z])(\d+)", b_id)
            if match:
                return match.group(1), int(match.group(2))
            # Fallback for IDs that don't match the pattern (e.g., "Error", "123")
            return "B", 0

        try:
            # 2. Find the 'max' using our safe parser
            last_record = max(self.bookings, key=safe_parse_id)
            letter, last_number = safe_parse_id(last_record)
            
            # 3. Increment
            next_number = last_number + 1
            
            # 4. Format with padding (e.g., 2 -> "0002")
            return f"{letter}{next_number:04d}"

        except Exception as e:
            # 5. Extreme Fallback: If everything fails, generate a timestamp-based ID 
            # or a simple count-based ID to prevent the app from crashing.
            return f"B{len(self.bookings) + 1:04d}"
    
    def get_field_cost(self, field_id):
        return self.field_manager.field_cost(field_id)
    
    def calculate_hours(self,start,end):
        t1 = datetime.strptime(start,"%H:%M")
        t2 = datetime.strptime(end,"%H:%M")

        diff = t2 - t1

        return diff.seconds / 3600
    def _check_availability(self, field_id,booking_date ,start, end):

        for b in self.bookings:
            if b.field_id != field_id:
                continue
            if b.booking_status != "cancelled":
                continue
            if b.booking_date !=booking_date:
                continue
            if start < b.booking_time_end and end > b.booking_time_start:
                return False
        return True 
    def check_customer_active(self, customer_id):
        return self.customer_manager.check_customer_active(customer_id)
    
    def check_field_active(self, field_id):
        return self.field_manager.check_field_active(field_id)
    
    def add_booking(self, start, end, customer_id, field_id):       
        if not self.check_customer_active(customer_id) and not self.check_field_active(field_id):
            return
        booking_id =self.generate_booking_id()
        print(f"Booking ID: ", booking_id)
        booking_date = datetime.now().strftime("%Y-%m-%d")

        if not self._check_availability(field_id,booking_date, start, end):
            print("Field not available in this time")
            return
        
        field_cost = self.get_field_cost(field_id)
        if field_cost is None:
            print("Field not found")
            return
        
        hours = self.calculate_hours(start, end)
        total_price = hours * field_cost

        booking = BookingRecord(
            booking_id,
            field_id,
            customer_id,
            datetime.now().strftime("%Y-%m-%d"),
            start,    
            end,
            total_price,
            "confirmed",  
        )

        self.bookings.append(booking)
        self.save_booking()
        print("Booking added successfully")
        
    def edit_booking_status(self, booking_id, status):
        for b in self.bookings:
            if b.booking_id == booking_id:
                b.booking_status = status
                self.save_booking()
                print("Booking status updated")
                return
        print("Booking not found")
    def view_booking_list(self, status=None):
        if not self.bookings:
            print("No booking")
            return

        print("ID        Date        Status      Start      End        Price    Customer    Field")
        print("-"*85)

        for b in self.bookings:
            if status and b.booking_status != status:
                continue
            print(b)
    def get_booking_by_id(self, booking_id):
        for b in self.bookings:
            if b.booking_id == booking_id:
                return b
        return None
    
    def menu(self):
        while True:
            print("\n===== BOOKING MANAGEMENT =====")
            print("1 Add booking")
            print("2 View booking")
            print("3 Change booking status")
            print("0 <<<Back")

            choice = input("Choose: ")
            if choice == "1":
                start = input("Start time (HH:MM): ")
                end = input("End time (HH:MM): ")
                cus = input("Customer ID: ")
                field = input("Field ID: ")

                self.add_booking(start, end, cus, field)

            elif choice == "2":

                self.view_booking_list()

            elif choice == "3":

                bid = input("Booking ID: ")
                status = input("Status (confirmed/cancelled): ")

                self.edit_booking_status(bid, status)

            elif choice == "0":
                break


if __name__ == "__main__":
    BookingManagement().menu()
