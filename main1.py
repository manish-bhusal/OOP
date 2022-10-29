# ATM MACHINE
class Atm:
    def __init__(self) -> None:
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = """
        Hello, How would you like to proceed?
        1. Enter 1 to create pin.
        2. Enter 2 to deposit.
        3. Enter 3 to withdraw.
        4. Enter 4 to check balance.
        5. Enter 5 to exit
        """
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit_money()
        elif user_input == 3:
            self.withdraw_money()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            print("Bye! Have a nice day.")
        # else:
        #     print("Please enter valid number. Thank you!")

    def create_pin(self):
        self.pin = input("Create your PIN: ")
        print("Pin set successfully.")

    def deposit_money(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid pin.")

    def withdraw_money(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if self.balance > amount:
                self.balance -= amount
                print("Operation Successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid pin.")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin.")
