#Accounts Handling
#Create class to handle actions that you can perform on the account
class MainAccount:
    def __init__(self, holder, account_id, balance=0):
        self.holder = holder
        self.account_id = account_id
        self.balance = balance

#Define a function to view all the details on the account
    def view_account_details(self):
        return f"User: {self.holder}\nAccount ID: {self.account_id}\nBalance: ${self.balance}"
    
 #Define a function to deposit into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New Balance: ${self.balance}"
        return "Deposit amount must be greater than 0"  

#Define a function that allows the holder to withdraw money
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "You do not have enough in the balance or you enetered in an invalid amount."
    
#create a class to have a savings account, it is inherited from main account
class SavingsAccount(MainAccount):
    def __init__(self, holder, account_id, balance=0, interest_rate=0.04):
        super().__init__(holder, account_id, balance)
        self.interest_rate = interest_rate

#Create a function that allows interest to be added into a sitting balance
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Add interest amount: ${interest}. New balance with added interest is ${self.balance}"
    
#Create a function for Checking account
class CheckingsAccount(MainAccount):
    def __init__(self, holder, account_id, balance=0, overdraft_limit=5):
       super().__init__(holder, account_id, balance)
       self.overdraft_limit = overdraft_limit

#Create a function for withdrawing from checking account
    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.overdraft_limit:
            self.balance -= amount
            return f"Withdraw ${amount}. New balance is ${self.balance}"
        return "Invalid amount or went over the set overdraft amount."

#Create a function seperate from the classes to create an account
def create_account(account_type, holder, account_id, initial_balance=0):
        #use if else statement to give option to the type of account they are making
    if account_type.lower() == "savings":
         return SavingsAccount(holder, account_id, initial_balance)
    elif account_type.lower() == "checking" or account_type.lower() == "checkings":
        return CheckingsAccount(holder, account_id, initial_balance)
    else:
        raise ValueError("Not a valid account type, please try again.")
        
    #Create a function that just displays account details
def display_account_details(account):
    return f"Account Details:\n{account.view_account_details()}"

#tests
if __name__ == "__main__":
    savings = create_account("savings", "Michael", "M001", 1000)
    checkings = create_account("checking", "Michael", "c001", 1200)

    display_account_details(savings)
    display_account_details(checkings)
    print(display_account_details(savings))
    print(display_account_details(checkings))
    print(savings.apply_interest())
    print(checkings.withdraw(250))
    print(checkings.withdraw(50))