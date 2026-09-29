import customer
import account
import deposit
import withdrawl
import transfer
import loan
import reports

def main():

    while True:

        print("\n========================================")
        print("       BANK MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Customer Management")
        print("2. Account Management")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Loan Management")
        print("7. Reports")
        print("8. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer.customer_menu()

        elif choice == "2":
            account.account_menu()

        elif choice == "3":
            deposit.deposit_money()

        elif choice == "4":
            withdrawl.withdraw_money()

        elif choice == "5":
            transfer.transfer_money()

        elif choice == "6":
            loan.loan_menu()

        elif choice == "7":
            reports.report_menu()

        elif choice == "8":
            print("\nThank you for using Bank Management System.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()