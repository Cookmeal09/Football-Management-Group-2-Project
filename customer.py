class Customer:
    def __init__(self, customer_id, name, field_id, booking_date, booking_time, phone, booking_count=1):
        self.customer_id = int(customer_id)
        self.name = name
        self.field_id = field_id
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.phone = phone
        self.booking_count = int(booking_count)

    def to_string(self):
        return f"{self.customer_id},{self.name},{self.field_id},{self.booking_date},{self.booking_time},{self.phone},{self.booking_count}"

    @staticmethod
    def from_string(data):
        parts = data.strip().split(",")
        return Customer(
            int(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            parts[5],
            int(parts[6])
        )

    def display(self):
        print(f"{self.customer_id:<10}{self.name:<20}{self.field_id:<10}{self.booking_date:<15}{self.booking_time:<10}{self.phone:<15}{self.booking_count:<10}")