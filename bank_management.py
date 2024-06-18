# write a program to manage all the operation in happen to the bank
# from ast import main
import uuid


class Bank_management:

    def __init__(self, account_holder, balance, IFSC_code, branch, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.IFCS_code = IFSC_code
        self.branch = branch
        self.account_number = account_number

    def credit_amount(self, amount):
        if amount < 0:
            print('Sorry!! enter the valid amount ')
            return

        self.balance = self.blanace + amount
        print(f"balance are credit successfully: {amount}\n"
              f"Total balance:{self.balance}")

    def debit_amount(self, amount):
        if amount > self.balance:
            print("insufficient amount!! \n"
                  f"Total available balance: {self.balance}")
            return
        elif amount < 0:
            print("invalid amount !! enter the valid amount")
            return

        else:
            self.balance = self.balance - amount
            print(f'balance debited successfully: {amount}',
                  f"Available balance:{self.amount}")

    def view_balance(self):
        print("total balance is;", self.amount)

    def view_account_details(self):
        print(f"Account Number: {self.account_number}\n"
              f"Account Holder Name: {self.account_holder}\n"
              f"Balance: {self.balance}\n"
              f"IFSC CODE: {self.IFSC_code}\n"
              f"Branch Name: {self.branch}")


def main():
    print("Welcome To the Bank\n")
    print("Enter the Bank Details\n")

    account_number = uuid.uuid4()
    account_holder_name = input("Please Enter the holder name: ")
    ifsc_code = "110BFS001"
    branch = "abc branch"
    balance = float(input("Please Enter the Initial Balance: "))

    bank_obj = Bank_management(account_holder_name, ifsc_code, balance, branch, account_number)
    while True:
        print(f"1. Credit Amount\n"
              f"2. Debit Amount\n"
              f"3. View Bank Details\n"
              f"4. View Bank Balance\n"
              f"5. EXIT")

        choice = int(input("Please Choose: "))

        if choice == 1:
            amount = float(input("Please Enter the Amount:: "))
            bank_obj.credit_amount(amount)
        elif choice == 2:
            amount = float(input("Please Enter the Amount:: "))
            bank_obj.debit_amount(amount)
        elif choice == 3:
            bank_obj.view_account_details()
        elif choice == 4:
            bank_obj.view_balance()
        elif choice == 5:
            break
        else:
            print("Invalid Choice!!!!!!!!")
            break
