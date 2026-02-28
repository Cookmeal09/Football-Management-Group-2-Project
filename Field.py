class Field:
    def __init__(self, field_id, name, field_type, cost, status, is_booking=False):
        self.field_id = field_id
        self.name = name
        self.field_type = field_type
        self.cost = cost
        self.status = status
        self.is_booking = is_booking  # mặc định chưa có người đặt

    def to_string(self):
        return f"{self.field_id},{self.name},{self.field_type},{self.cost},{self.status},{self.is_booking}"

    @staticmethod
    def from_string(data):
        parts = data.strip().split(",")
        return Field(
            parts[0],
            parts[1],
            parts[2],
            float(parts[3]),
            parts[4],
            parts[5] == "True"
        )

    def display(self):
        booking_text = "Yes" if self.is_booking else "No"
        print(f"{self.field_id:<10}{self.name:<15}{self.field_type:<10}{self.cost:<15}{self.status:<15}{booking_text:<10}")