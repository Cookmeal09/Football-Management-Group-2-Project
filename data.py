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
    """
    Data Entry Order:
    1. customer_id (str): Unique identifier
    2. customer_name (str): Human-readable name
    3. phone (str): Contact information
    4. customer_status (str): Current state (e.g., 'Active', 'Inactive')

    """
    customer_id: str   
    customer_name: str
    phone: str
    customer_status: str = "active"

    def to_string(self) -> str:
        return f"{self.customer_id},{self.customer_name},{self.phone},{self.customer_status}"

    @staticmethod
    def from_string(data: str) -> "CustomerRecord":
        parts = data.strip().split(",")
        return CustomerRecord(
        parts[0],
        parts[1],
        parts[2],
        parts[3] if len(parts) > 3 else "active"
    )

    def __str__(self):
        return  f"{self.customer_id:<10}{self.customer_name:<20}{self.phone:<15}{self.customer_status:<10}"

@dataclass
class FieldRecord:
    """
    Represents a standardized field entry.
    
    Data Entry Order:
    1. field_id (str): Unique identifier
    2. field_name (str): Human-readable name
    3. field_type (str): Category/Classification
    4. field_cost (float): Price or operational cost
    5. field_status (str): Current state (e.g., 'Active', 'Inactive')
    """
    field_id: str
    field_name: str
    field_type: str
    field_cost: float
    field_status: str = "Active"

    def to_string(self) -> str:
        return f"{self.field_id},{self.field_name},{self.field_type},{self.field_cost},{self.field_status}"

    def __str__(self):
        return "{:<10}{:<12}{:<10}{:<10.2f}{:<12}".format(self.field_id, self.field_name, self.field_type, self.field_cost, self.field_status)
    
    @staticmethod
    def from_string(data: str) -> "FieldRecord":
        parts = data.strip().split(",")
        return FieldRecord(
            parts[0],
            parts[1],
            parts[2],
            float(parts[3]),
            parts[4],
        )


@dataclass
class BookingRecord:
    """
    Data record for a field booking.
    
    Data Entry Order:
    1. booking_id (str): Unique booking reference.
    2. field_id (str): ID of the reserved field.
    3. customer_id (str): ID of the customer.
    4. booking_date (str): Date of the reservation.
    5. booking_time_start (str): Start timestamp (Default: Now).
    6. booking_time_end (str): End timestamp (Default: Now).
    7. booking_total_price (float): Total cost (Default: 0.0).
    8. booking_status (str): Status string (Default: 'Booked').
    """
    booking_id: str
    field_id: str
    customer_id: str
    booking_date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    booking_time_start: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    booking_time_end: str= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    booking_total_price: float = 0.0
    booking_status: str = "Booked"

    
    def to_string(self) -> str:
        return f"{self.booking_id},{self.field_id},{self.customer_id},{self.booking_date},{self.booking_time_start},{self.booking_time_end}, {self.booking_total_price},{self.booking_status}"

    def __str__(self) -> str:
        return f"{self.booking_id:<10}{self.booking_date:<12}{self.booking_status:<12}{self.booking_time_start:<10}{self.booking_time_end:<10}{self.booking_total_price:<12.2f}{self.customer_id:<10}{self.field_id:<10}"
    
    @staticmethod
    def from_string(data: str) -> "BookingRecord":
        parts = data.strip().split(",")
        return BookingRecord(
            parts[0],
            parts[1],
            parts[2],
            parts[3],
            parts[4] if len(parts) > 3 else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            parts[5] if len(parts) > 4 else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            float(parts[6]),
            parts[7] if len(parts) > 6 else "Booked",

        )

@dataclass
class PaymentRecord:
    """
    Data record for a payment transaction.
    
    Data Entry Order:
    1. payment_id (str): Unique transaction reference.
    2. booking_id (str): Reference to the associated booking.
    3. payment_method (str): Method used (e.g., 'Credit Card', 'Cash').
    4. payment_total (float): Total amount paid.
    5. payment_status (str): Current status (e.g., 'Completed', 'Pending').
    6. payment_date (str): Timestamp of the payment (Default: Current Time).
    """
    payment_id: str
    booking_id: str
    payment_method: str
    payment_total: float
    payment_status: str
    payment_date: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_string(self) -> str:
        return f"{self.payment_id},{self.booking_id},{self.payment_method},{self.payment_total},{self.payment_status},{self.payment_method},{self.payment_date}"

    def __str__(self):
        return "{:<10}{:<12}{:<10}{:<10}{:<10.2f}{:<12}".format(
        self.payment_id,
        self.payment_method,
        self.payment_status,
        self.payment_date,
        self.payment_total,
        self.booking_id,
    )
    
    @staticmethod
    def from_string(data: str) -> "PaymentRecord":
        parts = data.strip().split(",")
        return PaymentRecord(
            parts[0],
            parts[1],
            parts[2],
            float(parts[3]),
            parts[4],
            parts[5] if len(parts) > 4 else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )


# =========================
# Save helpers
# =========================

def _save_records(records, filename: str):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for record in records:
                # We assume record has a to_string() method defined
                f.write(record.to_string() + "\n")
        print(f"Successfully saved {len(records)} records to {filename}.")

    except PermissionError:
        print(f"Error: You do not have permission to write to '{filename}'. Is it open in another program?")
    except FileNotFoundError:
        print(f"Error: The directory for '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred while saving: {e}")

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

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                
                try:
                    # Attempt to convert the line into a record object
                    record = record_cls.from_string(line)
                    records.append(record)
                except (ValueError, IndexError, TypeError) as e:
                    # This catches issues with a SPECIFIC line (bad data)
                    # but allows the loop to continue to the next line.
                    print(f"Skipping line {line_number} in {filename}: Malformed data. ({e})")
                    continue

    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    except Exception as e:
        # This catches "Big" errors, like the file being corrupted 
        # or the computer losing connection to the drive.
        print(f"A critical error occurred while loading {filename}: {e}")
        
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
    
    save_customer_to_file([CustomerRecord("A1", "Nguyen Van A", "0123456789", "active")])
    # đọc lại
    data = load_customer_from_file()

    print("Loaded data:")
    for c in data:
        print(c)
