##Create a custom exception named `InsufficientBalanceError`. 
#In the `BankAccount` class, raise this exception when a withdrawal amount is greater than the balance.
#Handle the exception and print an appropriate message.
class InsufficientBAlanceError(Exception):
    pass
class BankAccount():
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self,money):
        if money>0:
            self.__balance += money
        print(f"Your new balance is {self.__balance}")
    def withdraw(self,amount):
        try:
            if amount > self.__balance:
                raise InsufficientBAlanceError
            else:
                self.__balance -= amount
                print("Money debited from your account")
        except InsufficientBAlanceError:
            print("Your cannot withdraw more than available balance")
    def check_balance(self):
        print(f"Your balance is: {self.__balance}")
a1 = BankAccount(111,0)
a1.withdraw(100)
a1.deposit(10000)
a1.check_balance()
a1.withdraw(5000)
a1.check_balance()