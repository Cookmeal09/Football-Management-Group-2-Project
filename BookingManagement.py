from dataclasses import dataclass , field # tạo constructor tự động
import datetime # để lấy thời gian hiện tại
@dataclass 
class Booking: # tạo class Booking với các thuộc tính và phương thức
    booking_id: str
    field: object
    customer: object
    date: str
    schedule: str
    _status: str = field(default=" ")
    created_time: datetime.datetime = field(default_factory=datetime.now())

    @property # cho phép dùng 1 hàm như 1 biến
    def status(self):
        return self._status # _status là biến private để lưu trữ trạng thái thực tế của booking

    @status.setter # cho phép gán giá trị cho biến status nhưng có thể kiểm tra giá trị trước khi gán
    def status(self, value): 
        if value not in ["Booked", "In Use", "Completed", "Cancelled"]: # kiểm tra nếu giá trị không hợp lệ thì sẽ báo lỗi
            raise ValueError("Invalid status") # nếu giá trị ko hợp lệ thì sẽ báo lỗi ngay. 
        self._status = value # nếu giá trị hợp lệ thì sẽ gán giá trị cho biến _status

    def __str__(self): # định nghĩa lại phương thức __str__ để khi in đối tượng Booking sẽ hiển thị thông tin chi tiết của booking
        return (f"Booking ID: {self.booking_id} | "
                f"Field: {self.field.name} | "
                f"Customer: {self.customer.name} | "
                f"Date: {self.date} | "
                f"Schedule: {self.schedule} | "
                f"Status: {self._status}")


# =========================
# BOOKING MANAGER
# =========================
class BookingManager:
    def __init__(self, field_list, customer_list):
        self.bookings = []
        self.field_list = field_list 
        self.customer_list = customer_list

    # ADD BOOKING
    def addBooking(self, booking_id, field_id, customer_id, date, schedule):
        try:
            field = next(f for f in self.field_list if f["field_id"] == field_id) # tìm kiếm sân theo field_id trong danh sách field_list, nếu không tìm thấy sẽ ném ra lỗi StopIteration
            customer = next(c for c in self.customer_list if c["customer_id"] == customer_id)
        except StopIteration:
            print("Field ID or Customer ID not found!")
            return

        if field["status"] != "Available": 
            print("Field is not available!")
            return

        new_booking = Booking(booking_id, field, customer, date, schedule)
        self.bookings.append(new_booking)
        field["status"] = "Booked"
        field.is_booking = True

        print("Booking added successfully!")

    # DISPLAY BOOKING
    def displayBooking(self):
        print("=== Current Active Bookings ===")
        for booking in self.bookings:
            if booking.status in ["Booked", "In Use"]:
                print(booking)

    # EDIT BOOKING (CHANGE STATUS ONLY)
    def editBooking(self, booking_id, new_status):
        for booking in self.bookings:
             if booking.booking_id == booking_id:
                booking.status = new_status

                # cập nhật trạng thái sân
                if new_status in ["Completed", "Cancelled"]:
                    booking.field.status = "Available"
                    booking.field.is_booking = False
                elif new_status == "In Use":
                    booking.field.status = "In Use"

                print("Booking status updated!")
                return

        print("Booking ID not found!")

    # FIND BOOKING
    def findBooking(self, keyword):
        print("=== Search Result ===")
        for booking in self.bookings:
            if (keyword == booking.booking_id or
                str(keyword) == str(booking.customer.customer_id) or
                keyword.lower() in booking.customer.name.lower()):
                print(booking)
