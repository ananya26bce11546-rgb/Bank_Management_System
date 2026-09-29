import json
import os


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


def create_account():
    data = load_data()

    print("\n---------- CREATE ACCOUNT ----------")

    customer_id = input("Enter Customer ID: ")

    customer_found = False

    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
            customer_found = True
            break

    if not customer_found:
        print("Customer does not exist.")
        print("Please register the customer first.")
        return

    account_number = input("Enter Account Number: ")

    for account in data["accounts"]:
        if account["account_number"] == account_number:
            print("Account number already exists.")
            return

    print("\nSelect Account Type")
    print("1. Savings Account")
    print("2. Current Account")

    account_choice = input("Enter choice: ")

    if account_choice == "1":
        account_type = "Savings"
    elif account_choice == "2":
        account_type = "Current"
    else:
        print("Invalid account type.")
        return

    try:
        initial_balance = float(input("Enter Initial Deposit: "))

        if initial_balance < 0:
            print("Amount cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    account = {
        "account_number": account_number,
        "customer_id": customer_id,
        "account_type": account_type,
        "balance": initial_balance
    }

    data["accounts"].append(account)
    save_data(data)

    print("\nAccount created successfully.")
    print("Account Number:", account_number)


def view_accounts():
    data = load_data()

    print("\n---------- ACCOUNT LIST ----------")

    if len(data["accounts"]) == 0:
        print("No accounts found.")
        return

    for account in data["accounts"]:
        print("--------------------------------")
        print("Account Number :", account["account_number"])
        print("Customer ID    :", account["customer_id"])
        print("Account Type   :", account["account_type"])
        print("Balance        :", account["balance"])


def check_balance():
    data = load_data()

    account_number = input("\nEnter Account Number: ")

    for account in data["accounts"]:
        if account["account_number"] == account_number:
            print("\nAccount Number:", account["account_number"])
            print("Current Balance:", account["balance"])
            return

    print("Account not found.")


def account_menu():
    while True:
        print("\n========== ACCOUNT MANAGEMENT ==========")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Check Balance")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            view_accounts()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")