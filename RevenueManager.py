import pandas as pd
from datetime import datetime
import os

FILENAME = "revenue_sample.txt"

# Tạo file nếu chưa có
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=[
        "revenue_id", "field_id", "customer_id",
        "booking_id", "amount",
        "payment_method", "payment_status", "created_time"
    ])
    df.to_csv(FILENAME, index=False)


# function

def add_revenue():
    revenue_id = input("Enter Revenue ID: ")
    field_id = input("Enter Field ID: ")
    customer_id = input("Enter Customer ID: ")
    booking_id = input("Enter Booking ID: ")
    amount = float(input("Enter Amount: "))
    payment_method = input("Payment Method (cash/bank_transfer): ")
    payment_status = input("Payment Status (paid/unpaid): ")
    created_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_data = {
        "revenue_id": revenue_id,
        "field_id": field_id,
        "customer_id": customer_id,
        "booking_id": booking_id,
        "amount": amount,
        "payment_method": payment_method,
        "payment_status": payment_status,
        "created_time": created_time
    }

    df = pd.read_csv(FILENAME)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(FILENAME, index=False)

    print("Revenue added successfully!\n")


def view_all():
    df = pd.read_csv(FILENAME)
    if df.empty:
        print("No revenue data found.\n")
    else:
        print("\nALL REVENUE DATA")
        print(df)
        print("============================\n")


def total_revenue_by_date():
    date_input = input("Enter date (YYYY-MM-DD): ")

    df = pd.read_csv(FILENAME)
    df["created_time"] = pd.to_datetime(df["created_time"])

    selected_date = pd.to_datetime(date_input).date()

    filtered = df[
        (df["created_time"].dt.date == selected_date) &
        (df["payment_status"] == "paid")
    ]

    print(f"\n REVENUE REPORT {selected_date}")
    print(filtered)
    total = filtered["amount"].sum()
    print("==========================================")
    print(f"Total Revenue: {total}\n")


def delete_revenue():
    revenue_id = input("Enter Revenue ID to delete: ")
    df = pd.read_csv(FILENAME)

    if revenue_id in df["revenue_id"].values:
        df = df[df["revenue_id"] != revenue_id]
        df.to_csv(FILENAME, index=False)
        print("Deleted successfully!\n")
    else:
        print("Revenue ID not found.\n")


# ================= MENU =================

def menu():
    while True:
        print("====== REVENUE MANAGEMENT ======")
        print("1. Add Revenue")
        print("2. View All Revenue")
        print("3. Total Revenue By Date")
        print("4. Delete Revenue")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            add_revenue()
        elif choice == "2":
            view_all()
        elif choice == "3":
            total_revenue_by_date()
        elif choice == "4":
            delete_revenue()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run chương trình
menu()