##Create a class named `BankAccount` with private attributes `account_number` and `balance`. 
#Add methods to deposit and withdraw money, and to check the balance. Create an object of the class and perform some operations.

class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self,money):
        if money>0:
            self.__balance += money
        print(f"Your new balance is {self.__balance}")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance in your account")
        else:
            self.__balance -= amount
            print("Money debited from your account")
    def check_balance(self):
        print(f"Your balance is: {self.__balance}")
a1 = BankAccount(111,0)
a1.deposit(10000)
a1.check_balance()
a1.withdraw(5000)
a1.check_balance()
