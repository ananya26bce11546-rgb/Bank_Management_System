Bank Management System

Project Overview

The Bank Management System is a simple, console-based application developed using Python. The project is designed to show basic Python programming concepts through a practical banking application.

This project doesn't use a GUI, database, internet connection, or any external service. All information is stored locally in a JSON file.

Features

The system provides the following features:

Customer Management

Add a new customer

View all customers

Search for a customer

Account Management

Create a bank account

View all accounts

Check account balance

Deposit Money

Deposit money into an account

Automatically update the account balance

Store the transaction record

Withdraw Money

Withdraw money from an account

Check available balance

Prevent withdrawal when the balance is insufficient

Store the transaction record

Money Transfer

Transfer money between two accounts

Check sender and receiver accounts

Check available balance

Store both transfer records

Loan Management

Apply for a loan

Select different loan types

View loan applications

Reports

View account details

View transaction history

View overall bank summary

Technologies Used

Python 3

JSON

Python standard library

File handling

datetime

os

No external Python packages are required.

Project Structure

Bank_Management_System/
│
├── main.py
├── customer.py
├── account.py
├── deposit.py
├── withdrawal.py
├── transfer.py
├── loan.py
├── reports.py
├── bank_data.json
└── README.md

Module Description

1. main.py

This is the main program file. It displays the main menu and connects all other modules.

2. customer.py

This module manages customer information.

Functions include:

Add Customer

View Customers

Search Customer

3. account.py

This module manages bank accounts.

Functions include:

Create Account

View Accounts

Check Balance

4. deposit.py

This module handles deposits and updates the account balance.

5. withdrawal.py

This module handles withdrawals and checks whether enough balance is available.

6. transfer.py

This module allows money to be transferred from one bank account to another.

7. loan.py

This module handles loan applications and displays loan records.

8. reports.py

This module generates account reports, transaction history, and a general bank summary.

Data Storage

The project uses a file named bank_data.json to store information locally.

The initial structure of the file is:

{
    "customers": [],
    "accounts": [],
    "transactions": [],
    "loans": []
}

The program automatically updates this file whenever customer, account, transaction, or loan information is added.

Requirements

To run this project, you need:

Python 3.x

Any Python editor such as:

VS Code

PyCharm

IDLE

Thonny

No internet connection is required.

How to Run

Step 1: Create the project folder

Create a folder named:

Bank_Management_System

Step 2: Add the Python files

Place all eight Python modules inside the folder:

main.py
customer.py
account.py
deposit.py
withdrawal.py
transfer.py
loan.py
reports.py

Also create:

bank_data.json

Step 3: Add initial JSON data

Put the following in bank_data.json:

{
    "customers": [],
    "accounts": [],
    "transactions": [],
    "loans": []
}

Step 4: Run the program

Open a terminal inside the project folder and run:

python main.py

On some systems, you may need:

python3 main.py

Main Menu

After starting the program, the following menu will be displayed:

========================================
        BANK MANAGEMENT SYSTEM
========================================
1. Customer Management
2. Account Management
3. Deposit Money
4. Withdraw Money
5. Transfer Money
6. Loan Management
7. Reports
8. Exit
========================================
Enter your choice:

Sample Test Data

You can use the following information to test the project.

Customer 1

Customer ID: C001
Customer Name: Rahul Sharma
Phone Number: 9876543210
Address: Bhopal, Madhya Pradesh
Age: 19

Customer 2

Customer ID: C002
Customer Name: Aman Verma
Phone Number: 9123456780
Address: Indore, Madhya Pradesh
Age: 20

Account 1

Customer ID: C001
Account Number: 100001
Account Type: Savings
Initial Deposit: 10000

Account 2

Customer ID: C002
Account Number: 100002
Account Type: Savings
Initial Deposit: 15000

Sample Transactions

Deposit

Account Number: 100001
Amount: 5000

New balance:

15000

Withdrawal

Account Number: 100001
Amount: 2000

New balance:

13000

Transfer

Sender Account Number: 100001
Receiver Account Number: 100002
Amount: 3000

After the transfer:

Account 100001: 10000
Account 100002: 18000

Loan Application

Customer ID: C001
Loan Type: Education Loan
Loan Amount: 50000

Python Concepts Demonstrated

This project demonstrates several fundamental Python concepts:

Variables

Data types

Input and output

Conditional statements

if, elif, and else

for loops

while loops

Functions

Lists

Dictionaries

Modules

Import statements

File handling

JSON data handling

Exception handling

Date and time

Basic validation

Project Objectives

The main objectives of this project are:

To understand how Python modules work together.

To develop a practical application using Python.

To understand functions and modular programming.

To practice file handling and JSON data storage.

To put in place basic banking operations.

To understand input validation and error handling.

To develop problem-solving skills using Python.

Limitations

This is an educational project and isn't intended for real banking use.

The project:

doesn't use a database.

doesn't have a graphical user interface.

doesn't have internet connectivity.

doesn't provide real banking security.

doesn't use encryption or authentication.

Stores data locally in a JSON file.

Future Improvements

The project can be improved in the future by adding:

Login and password system

Admin and customer roles

Database connectivity

Graphical user interface

Account statement generation

Interest calculation

Loan repayment system

ATM simulation

Password encryption

Better input validation

Author

Bank Management System

Developed as a Python academic/project application.

License

This project is created for educational purposes.