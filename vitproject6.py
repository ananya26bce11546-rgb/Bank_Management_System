import json
import os
from datetime import datetime

FILE_NAME = "bank_data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return {
            "customers": [],
            "accounts": [],
            "transactions": [],
            "loans": []
        }

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {
            "customers": [],
            "accounts": [],
            "transactions": [],
            "loans": []
        }

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def apply_loan():
    data = load_data()

    print("\n---------- LOAN APPLICATION ----------")

    customer_id = input("Enter Customer ID: ")

    customer_found = False

    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
            customer_found = True
            break

    if not customer_found:
        print("Customer not found.")
        return

    print("\nLoan Types")
    print("1. Education Loan")
    print("2. Home Loan")
    print("3. Personal Loan")
    print("4. Vehicle Loan")

    choice = input("Select Loan Type: ")

    if choice == "1":
        loan_type = "Education Loan"
    elif choice == "2":
        loan_type = "Home Loan"
    elif choice == "3":
        loan_type = "Personal Loan"
    elif choice == "4":
        loan_type = "Vehicle Loan"
    else:
        print("Invalid choice.")
        return

    try:
        amount = float(input("Enter Loan Amount: "))

        if amount <= 0:
            print("Loan amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    loan_id = "L" + str(len(data["loans"]) + 1)

    loan = {
        "loan_id": loan_id,
        "customer_id": customer_id,
        "loan_type": loan_type,
        "amount": amount,
        "status": "Pending",
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    data["loans"].append(loan)
    save_data(data)

    print("\nLoan application submitted.")
    print("Loan ID:", loan_id)
    print("Status: Pending")

def view_loans():
    data = load_data()

    print("\n---------- LOAN RECORDS ----------")

    if len(data["loans"]) == 0:
        print("No loan records found.")
        return

    for loan in data["loans"]:
        print("--------------------------------")
        print("Loan ID     :", loan["loan_id"])
        print("Customer ID :", loan["customer_id"])
        print("Loan Type   :", loan["loan_type"])
        print("Amount      :", loan["amount"])
        print("Status      :", loan["status"])
        print("Date        :", loan["date"])

def loan_menu():
    while True:
        print("\n========== LOAN MANAGEMENT ==========")
        print("1. Apply for Loan")
        print("2. View Loans")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            apply_loan()

        elif choice == "2":
            view_loans()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
