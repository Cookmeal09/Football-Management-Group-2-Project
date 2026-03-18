class Payment:
    def __init__(self,payment_id, payment_method, payment_status, payment_date, payment_total, booking_id):
        self.payment_id = booking_id
        self.payment_method = booking_date
        self.payment_status = booking_status
        self.payment_date = booking_time_start
        self.payment_total = booking_time_end
        self.booking_id = booking_id
    def to_string(self):
        return f"{self.payment_id},{self.payment_method},{self.payment_status},{self.payment_date},{self.paymnet_total},{self.booking_id}"
    @staticmethod
    def from_string(data):
        part = data.strip().split(",")
        return Payment(
            part[0],
            part[1],
            part[2],
            part[3],
            float(part[4]),
            part[5]
        )
