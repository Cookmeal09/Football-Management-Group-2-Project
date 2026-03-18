import os
from datetime import datetime
from CustomerManager import CustomerManager

class Booking:
    def __init__(self,booking_id, booking_date, booking_status, booking_time_start, booking_time_end, booking_total_price , customer_id, field_id):
        self.booking_id = booking_id
        self.booking_date = booking_date
        self.booking_status = booking_status
        self.booking_time_start = booking_time_start
        self.booking_time_end = booking_time_end
        self.booking_total_price = booking_total_price
        self.customer_id = customer_id
        self.field_id = field_id
    def to_string(self):
        return f"{self.booking_id},{self.booking_date},{self.booking_status},{self.booking_time_start},{self.booking_time_end},{self.booking_total_price},{self.customer_id},{self.field_id}"
    @staticmethod
    def from_string(data):
        part = data.strip().split(",")
        return Booking(
            part[0],
            part[1],
            part[2],
            part[3],
            part[4],
            float(part[5]),
            part[6],
            part[7]
        )
    def display(self):
        print(f"{self.booking_id:<10}{self.booking_date:<12}{self.booking_status:<12}{self.booking_time_start:<10}{self.booking_time_end:<10}{self.booking_total_price:<12}{self.customer_id:<10}{self.field_id:<10}")
class BookingManagement:
    def __init__(self):
        self.bookings = []
        self.booking_file = "booking.txt"
        self.load_booking()
        self.customer_manager=CustomerManager()
    def load_booking(self):
        if not os.path.exists(self.booking_file):
            return
        with open(self.booking_file, "r", encoding="utf-8") as f:
            for line in f:
                self.bookings.append(Booking.from_string(line))
    def save_booking(self):
        with open(self.booking_file, "w", encoding="utf-8") as f:
            for b in self.bookings:
                f.write(b.to_string() + "\n")
    def generate_booking_id(self):
        if not self.bookings:
            return "B0001"
        last = max(self.bookings, key=lambda b: (b.booking_id[0], int(b.booking_id[1:])))
        last_id = last.booking_id
        letter = last_id[0]
        number = int(last_id[1:]) + 1
        return f"{letter}{number:04d}"
    def get_field_cost(self, field_id):

        with open("field.txt","r",encoding="utf-8") as f:

            for line in f:
                part = line.strip().split(",")

                if part[0] == field_id:
                    return float(part[4])   # field_cost
        return None
    def calculate_hours(self,start,end):

        t1 = datetime.strptime(start,"%H:%M")
        t2 = datetime.strptime(end,"%H:%M")

        diff = t2 - t1

        return diff.seconds / 3600
    def _check_availability(self, field_id,booking_date ,start, end):
        for b in self.bookings:
            if b.field_id != field_id:
                continue
            if b.booking_date !=booking_date:
                continue
            if b.booking_status == "cancelled":
                continue
            if start < b.booking_time_end and end > b.booking_time_start:
                return False
        return True 
    def check_customer_active(self, customer_id):
        return self.customer_manager.check_customer_active(customer_id)

    def add_booking(self, start, end, customer_id, field_id):
        
        if not self.check_customer_active(customer_id):
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
        booking = Booking(
            booking_id,
            datetime.now().strftime("%Y-%m-%d"),
            "confirm",
            start,
            end,
            total_price,
            customer_id,
            field_id
        )
        self.bookings.append(booking)
        self.save_booking()
        print("Booking added successfully")
    def edit_booking_status(self, booking_id, status):

        for b in self.bookings:

            if b.booking_id == booking_id:

                b.booking_status = status

                self.save_booking()

                print("Booking updated")

                return

        print("Booking not found")
    def view_booking_list(self, status=None):

        if not self.bookings:
            print("No booking")
            return

        print("ID        Date        Status      Start      End        Price    Customer Field")
        print("-"*85)

        for b in self.bookings:

            if status and b.booking_status != status:
                continue

            b.display()
def main():

    manager = BookingManagement()

    while True:

        print("\n===== BOOKING MANAGEMENT =====")
        print("1 Add booking")
        print("2 View booking")
        print("3 Change booking status")
        print("0 Exit")

        choice = input("Choose: ")

        if choice == "1":

            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")
            cus = input("Customer ID: ")
            field = input("Field ID: ")

            manager.add_booking(start, end, cus, field)

        elif choice == "2":

            manager.view_booking_list()

        elif choice == "3":

            bid = input("Booking ID: ")
            status = input("Status (confirmed/cancelled): ")

            manager.edit_booking_status(bid, status)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
