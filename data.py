import os
from dataclasses import dataclass
from datetime import datetime

# Default filenames for each data category
CUSTOMER_FILE = "customer.txt"
FIELD_FILE = "field.txt"
BOOKING_FILE = "booking.txt"
PAYMENT_FILE = "payment.txt"


@dataclass
class CustomerRecord:
    customer_id: int
    name: str
    field_id: str
    booking_date: str
    booking_time: str
    phone: str
    booking_count: int = 1

    def to_string(self) -> str:
        return f"{self.customer_id},{self.name},{self.field_id},{self.booking_date},{self.booking_time},{self.phone},{self.booking_count}"

    @staticmethod
    def from_string(data: str) -> "CustomerRecord":
        parts = data.strip().split(",")
        return CustomerRecord(
            int(parts[0]),
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            parts[5],
            int(parts[6]) if len(parts) > 6 and parts[6] != "" else 1,
        )


@dataclass
class FieldRecord:
    field_id: str
    name: str
    field_type: str
    cost: float
    status: str
    is_booking: bool = False

    def to_string(self) -> str:
        return f"{self.field_id},{self.name},{self.field_type},{self.cost},{self.status},{self.is_booking}"

    @staticmethod
    def from_string(data: str) -> "FieldRecord":
        parts = data.strip().split(",")
        return FieldRecord(
            parts[0],
            parts[1],
            parts[2],
            float(parts[3]),
            parts[4],
            parts[5].strip().lower() == "true",
        )


@dataclass
class BookingRecord:
    booking_id: str
    field_id: str
    customer_id: str
    date: str
    schedule: str
    status: str = "Booked"
    created_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_string(self) -> str:
        return f"{self.booking_id},{self.field_id},{self.customer_id},{self.date},{self.schedule},{self.status},{self.created_time}"

    @staticmethod
    def from_string(data: str) -> "BookingRecord":
        parts = data.strip().split(",")
        return BookingRecord(
            parts[0],
            parts[1],
            parts[2],
            parts[3],
            parts[4],
            parts[5] if len(parts) > 5 else "Booked",
            parts[6] if len(parts) > 6 else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )


@dataclass
class PaymentRecord:
    payment_id: str
    field_id: str
    customer_id: str
    booking_id: str
    amount: float
    payment_method: str
    payment_status: str
    created_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_string(self) -> str:
        return f"{self.payment_id},{self.field_id},{self.customer_id},{self.booking_id},{self.amount},{self.payment_method},{self.payment_status},{self.created_time}"

    @staticmethod
    def from_string(data: str) -> "PaymentRecord":
        parts = data.strip().split(",")
        return PaymentRecord(
            parts[0],
            parts[1],
            parts[2],
            parts[3],
            float(parts[4]),
            parts[5],
            parts[6],
            parts[7] if len(parts) > 7 else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )


# =========================
# Save helpers
# =========================

def _save_records(records, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        for record in records:
            f.write(record.to_string() + "\n")


def save_customer_to_file(customers, filename: str = CUSTOMER_FILE):
    """Save a list of CustomerRecord objects to a text file."""
    _save_records(customers, filename)


def save_field_to_file(fields, filename: str = FIELD_FILE):
    """Save a list of FieldRecord objects to a text file."""
    _save_records(fields, filename)


def save_booking_to_file(bookings, filename: str = BOOKING_FILE):
    """Save a list of BookingRecord objects to a text file."""
    _save_records(bookings, filename)


def save_payment_to_file(payments, filename: str = PAYMENT_FILE):
    """Save a list of PaymentRecord objects to a text file."""
    _save_records(payments, filename)


# =========================
# Load helpers
# =========================

def _load_records(filename: str, record_cls):
    records = []
    if not os.path.exists(filename):
        return records
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(record_cls.from_string(line))
    return records


def load_customer_from_file(filename: str = CUSTOMER_FILE):
    """Load a list of CustomerRecord objects from a text file."""
    return _load_records(filename, CustomerRecord)


def load_field_from_file(filename: str = FIELD_FILE):
    """Load a list of FieldRecord objects from a text file."""
    return _load_records(filename, FieldRecord)


def load_booking_from_file(filename: str = BOOKING_FILE):
    """Load a list of BookingRecord objects from a text file."""
    return _load_records(filename, BookingRecord)


def load_payment_from_file(filename: str = PAYMENT_FILE):
    """Load a list of PaymentRecord objects from a text file."""
    return _load_records(filename, PaymentRecord)
if __name__ == "__main__":
    # tạo dữ liệu test
    customers = [
        CustomerRecord(1, "Nguyen Van A", "F001", "2026-03-20", "18:00", "0901234567"),
        CustomerRecord(2, "Tran Thi B", "F002", "2026-03-21", "19:00", "0912345678")
    ]

    # lưu file
    save_customer_to_file(customers)

    # đọc lại
    data = load_customer_from_file()

    print("Loaded data:")
    for c in data:
        print(c)