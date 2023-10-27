#craeting class bankaccount
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
#deposit constructor
    def deposit(self, amount):
        self.balance += amount
        return amount
#the withdraw method
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount
#the check_balance method
    def check_balance(self):
        print("Current balance:", self.balance)
#customers_details method 
    def customer_details(self):
        print("Customer name:", self.customer_name)
        print("Account number:", self.account_number)
        print("Date of opening:", self.date_of_opening)
        print("Balance:", self.balance)
        # Creating a new bank account
account = BankAccount(116234567,2999,"2022-05-02","Wangeshi")

# Deposit 500
amount_deposited = account.deposit(500)
print("Amount deposited:", amount_deposited)

# Withdraw 20000
amount_withdrawn = account.withdraw(20000)
print("Amount withdrawn:", amount_withdrawn)

# Check balance
account.check_balance()

# Print customer details
account.customer_details()