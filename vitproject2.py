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


def add_customer():
    data = load_data()

    print("\n---------- ADD CUSTOMER ----------")

    customer_id = input("Enter Customer ID: ")

    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
            print("Customer ID already exists.")
            return

    name = input("Enter Customer Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    age = input("Enter Age: ")

    customer = {
        "customer_id": customer_id,
        "name": name,
        "phone": phone,
        "address": address,
        "age": age
    }

    data["customers"].append(customer)
    save_data(data)

    print("\nCustomer added successfully.")


def view_customers():
    data = load_data()

    print("\n---------- CUSTOMER LIST ----------")

    if len(data["customers"]) == 0:
        print("No customers found.")
        return

    for customer in data["customers"]:
        print("--------------------------------")
        print("Customer ID :", customer["customer_id"])
        print("Name        :", customer["name"])
        print("Phone       :", customer["phone"])
        print("Address     :", customer["address"])
        print("Age         :", customer["age"])


def search_customer():
    data = load_data()

    customer_id = input("\nEnter Customer ID to search: ")

    for customer in data["customers"]:
        if customer["customer_id"] == customer_id:
            print("\nCustomer Found!")
            print("Customer ID :", customer["customer_id"])
            print("Name        :", customer["name"])
            print("Phone       :", customer["phone"])
            print("Address     :", customer["address"])
            print("Age         :", customer["age"])
            return

    print("Customer not found.")


def customer_menu():
    while True:
        print("\n========== CUSTOMER MANAGEMENT ==========")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            search_customer()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")