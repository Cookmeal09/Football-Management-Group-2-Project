from data import save_payment_to_file, load_payment_from_file, load_booking_from_file, load_customer_from_file, PaymentRecord
from BookingManagement import BookingManagement

class PaymentManagement:
    def __init__(self):
        self.payments = load_payment_from_file()
        self.bookingManager = BookingManagement()
        
    # từ object sang string
    def save_payment(self):
        save_payment_to_file(self.payments)

    # tạo ID tự động
    def generate_payment_id(self):
        # 1. Immediate guard for empty list
        if not self.payments:
            return "P0001"

        def parse_payment_id(payment_obj):
            """Safely extracts (Letter, Number) from 'P0001'."""
            p_id = str(payment_obj.payment_id).strip()
            
            # Guard against empty strings or None values in the data
            if not p_id:
                return ("P", 0)
                
            try:
                prefix = p_id[0]
                # Try to convert everything after the first letter to an integer
                number = int(p_id[1:])
                return (prefix, number)
            except (ValueError, IndexError):
                # If the ID is just "P" or malformed like "P-ABC", 
                # we return 0 so max() can still function.
                return (p_id[0] if p_id else "P", 0)

        try:
            # 2. Find the highest ID using our safe helper
            last_record = max(self.payments, key=parse_payment_id)
            letter, last_number = parse_payment_id(last_record)
            
            # 3. Increment and format with 4-digit padding (0001)
            return f"{letter}{last_number + 1:04d}"

        except Exception:
            # 4. Final safety net: If max() fails, use the count to stay unique
            return f"P{len(self.payments) + 1:04d}"
    
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
            
            booking_id = input("Enter booking ID: ").strip()
            if not self.bookingManager.get_booking_by_id(booking_id):
                print("Booking not found!")
                return

            new_payment = PaymentRecord(payment_id, booking_id, payment_method,payment_total, payment_status, payment_date , )
            self.payments.append(new_payment)
            self.save_payment()
            
            print("Payment added successfully!")

        except Exception as e:
            print("Unexpected error in add_payment:", e)

    # chỉnh trạng thái thanh toán
    def edit_payment_status(self):
        try:
            if not self.payments:
                print("No payments found!")
                return
            
            print("\n=== Payment List ===")
            for p in self.payments:
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
                        save_payment_to_file(self.payments)
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
                for p in self.payments:
                    print(p)

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

    def menu(self):
        while True:
            print("\n=== Payment Management ===")
            print("1. Add Payment")
            print("2. Edit Payment Status")
            print("3. View Payment List")
            print("4. Calculate Total Revenue")
            print("0. Back to Main Menu")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.add_payment()
            elif choice == "2":
                self.edit_payment_status()
            elif choice == "3":
                self.view_payment_list()
            elif choice == "4":
                self.calc_total_revenue()
            elif choice == "0":
                break
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    manager = PaymentManagement()
    manager.menu()