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


def deposit_money():
    data = load_data()

    print("\n---------- DEPOSIT MONEY ----------")

    account_number = input("Enter Account Number: ")

    for account in data["accounts"]:

        if account["account_number"] == account_number:

            try:
                amount = float(input("Enter Amount to Deposit: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    return

            except ValueError:
                print("Please enter a valid amount.")
                return

            account["balance"] += amount

            transaction = {
                "account_number": account_number,
                "type": "Deposit",
                "amount": amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M")
            }

            data["transactions"].append(transaction)

            save_data(data)

            print("\nDeposit successful.")
            print("Deposited Amount:", amount)
            print("Current Balance:", account["balance"])

            return

    print("Account not found.")