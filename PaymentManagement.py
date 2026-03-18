from data import save_payments_to_file, load_payments_from_file, load_bookings_from_file, load_customers_from_file
import os

class Payment:
    def __init__(self, payment_id, payment_method, payment_status, payment_date, payment_total, booking_id):
        self.payment_id = payment_id
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.payment_date = payment_date
        self.payment_total = payment_total
        self.booking_id = booking_id
    def to_string(self):
        return f"{self.payment_id},{self.payment_method},{self.payment_status},{self.payment_date},{self.payment_total},{self.booking_id}"
    @staticmethod
    def from_string(self):
      part = data.strip().split(",")
      return Payment(
          part[0],
          part[1],
          part[2],
          part[3],
          float(part[4]),
          part[5]
    )
    def display(self):
      print("{:<10}{:<12}{:<10}{:<10}{:<10}{:<12}".format(
        self.payment_id,
        self.payment_method,
        self.payment_status,
        self.payment_date,
        self.payment_total,
        self.booking_id,
    ))
class PaymentManagement:
    def __init__(self):
        try:
            self.payments = load_payments_from_file()
        except Exception as e:
            print("Error loading payments:", e)
            self.payments = []

    # từ string sang object
    def load_payment(self):
        if not os.path.exists(self.payment_file):
            return
        with open(self.payment_file, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == "":
                continue
            try:
                self.payments.append(Payment.from_string(line))
            except:
                continue

    # từ object sang string
    def save_payment(self):
        with open(self.payment_file, "w", encoding="utf-8") as f:
            for i in self.payments:
                f.write(i.to_string() + "\n")

    # tạo ID tự động
    def generate_payment_id(self):
        if not self.payments:
            return "P0001"
        last = max(self.payment, key=lambda f: (f.payment_id[0], int(f.payment_id[1:])))
        last_id = last.payment_id
        letter = last_id[0]
        number = int(last_id[1:]) + 1
        return f"{letter}{number:04d}"
    
    # lấy tên khách cho phần add_payment
    def get_customer_name(customer_id, customers):
    for c in customers:
        if c.customer_id == customer_id:
            return c.customer_name
    return "Unknown"

    # thêm khoản thanh toán
    def add_payment(self):
        print("\n=== Add Payment ===")
        payment_id = self.generate_payment_id()
        print("Payment ID:", payment_id)
        try:
            payment_method = input("Enter payment method: ").strip()
            payment_status = input("Enter payment status (paid/unpaid): ").strip()
            if payment_status.lower() not in ["paid", "unpaid"]:
                print("Invalid status!")
                return
            
            payment_date = input("Enter payment date: ").strip()

            try:
                payment_total = float(input("Enter total amount: "))
            except ValueError:
                print("Invalid amount! Must be a number.")
                return
            
            bookings = load_bookings_from_file()
            customers = load_customers_from_file()
             
            if not bookings:
                print("No bookings available!")
                return
            
            customer_dict = {c.customer_id: c.customer_name for c in customers}
            
            print("\n=== Booking List ===")
            for b in bookings:
                customer_name = customer_dict.get(b.customer_id, customers)
                print(f"[{b.booking_id}] - Customer: {customer_name}")
                
            booking_id = input("Enter booking ID: ").strip()
            
            if not any(b.booking_id == booking_id for b in bookings):
                print("Booking ID not found!")
                return
            
            new_payment = Payment(payment_id, payment_method, payment_status, payment_date, payment_total, booking_id)
            self.payments.append(new_payment)
            try:
                save_payments_to_file(self.payments)
            except Exception as e:
                print("Error saving payment:", e)
                return
            
            print("Payment added successfully!")

        except Exception as e:
            print("Unexpected error in add_payment:", e)

    # chỉnh trạng thái thanh toán
    def edit_payment_status(self):
        #payment_dict = {p.payment_id: p.payment_status for p in payments}
        try:
            if not self.payments:
                print("No payments found!")
                return
            
            print("\n=== Payment List ===")
            for p in payments:
                print(f"[{p.payment_id}] - Status: {p.payment_status}")
                
            payment_id = input("Enter payment ID to update: ").strip()

            for p in self.payments:
                if p.payment_id == payment_id:
                    new_status = input("Enter new status (paid/unpaid): ").strip()

                    if new_status.lower() not in ["paid", "unpaid"]:
                        print("Invalid status!")
                        return

                    p.payment_status = new_status

                    try:
                        save_payments_to_file(self.payments)
                    except Exception as e:
                        print("Error saving changes:", e)
                        return

                    print("Payment status updated!")
                    return

            print("Payment not found!")

        except Exception as e:
            print("Unexpected error in edit_payment_status:", e)

    # Xem danh sách các khoản thanh toán
    def view_payment_list(self):
        try:
            if not self.payments:
                print("No payments found!")
                return
            
            print("\n=== Payment List ===")
            for p in self.payments:
                print("{:<10}{:<12}{:<10}{:<10}{:<10}{:<12}".format(
                    "ID",
                    "Method",
                    "Status",
                    "Date",
                    "Total",
                    "Booking ID"
                ))
                print("-" * 60)
                for p in self.payment:
                    p.display()

        except Exception as e:
            print("Unexpected error in view_payment_list:", e)

    # tính tổng doanh thu
    def calc_total_revenue(self):
        try:
            total = 0

            for p in self.payments:
                try:
                    if p.payment_status.lower() == "paid":
                        total += float(p.payment_total)
                except Exception as e:
                    print("Error processing a payment:", e)

            print(f"Total revenue (paid only): {total}")
            return total

        except Exception as e:
            print("Unexpected error in calc_total_revenue:", e)
            return 0
