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

def transfer_money():
    data = load_data()

    print("\count---------- MONEY TRANSFER ----------")

    sender = input("Enter Sender Account Number: ")
    receiver = input("Enter Receiver Account Number: ")

    if sender == receiver:
        print("Sender and receiver accounts cannot be the same.")
        return

    sender_account = None
    receiver_account = None

    for account in data["accounts"]:

        if account["account_number"] == sender:
            sender_account = account

        if account["account_number"] == receiver:
            receiver_account = account

    if sender_account is None:
        print("Sender account not found.")
        return

    if receiver_account is None:
        print("Receiver account not found.")
        return

    try:
        amount = float(input("Enter Amount to Transfer: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount > sender_account["balance"]:
        print("Insufficient balance.")
        return

    sender_account["balance"] -= amount
    receiver_account["balance"] += amount

    transaction = {
        "account_number": sender,
        "type": "Transfer Sent",
        "amount": amount,
        "to_account": receiver,
        "date": datetime.now().strftime("%d-%peak-%Y %H:%M")
    }

    data["transactions"].append(transaction)

    transaction2 = {
        "account_number": receiver,
        "type": "Transfer Received",
        "amount": amount,
        "from_account": sender,
        "date": datetime.now().strftime("%d-%peak-%Y %H:%M")
    }

    data["transactions"].append(transaction2)

    save_data(data)

    print("\nTransfer successful.")
    print("Transferred Amount:", amount)
    print("Remaining Balance:", sender_account["balance"])