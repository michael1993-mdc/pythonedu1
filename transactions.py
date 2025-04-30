import json
import datetime


#Transactions
#Create functions that handle conditional statements
def deposits(account, amount):
    if amount <= 0:
        return "The amount you deposit has to be greater than."
    account['balance'] += amount
    return f"Deposited ${amount}. New balance is ${account['balance']}"

#now make the withdraw function
def withdraw(account, amount):
    if amount <= 0:
        return "Withdraw an amount greater than 0, if you have it!"
    if account['balance'] >= amount:
        account['balance'] -= amount
        return f"Withdrew ${amount}. Your new balance is ${account['balance']}"
    return "Sorry you don't have enough in your account for a withdrwal."

#make a function that helps moves funds between accounts
def transfer_funds(from_account, to_account, amount):
    if amount <= 0:
        return "Move an amount greater than 0"
    if from_account['balance'] >= amount:
        from_account['balance'] -= amount
        to_account['balance'] += amount
        return (f"Transferred ${amount} from {from_account['holder']} to {to_account['holder']}.\n"
                f"New balance - {from_account['holder']}: ${from_account['balance']},"
                f"{to_account['holder']}: ${to_account['balance']}")
    return "You don't have enough funds for this transfer."

#create a function to store the history of the transactions
def record_transaction(account_id, transaction_type, amount, transaction_history):
   transaction = {
       "account_id": account_id,
       "type": transaction_type,
       "amount": amount,
       "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   }
   transaction_history.append(transaction)

    #save to a json file
   with open('transactions.json', 'w') as file:
        json.dump(transaction_history, file)
   print("Transaction has been successfully executed.")


#create a function to retrieve the records we made
def load_transaction_history():
    try:
        with open('transactions.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
#tests
if __name__ == "__main__":
    account_a = {"holder": "Alice", "balance": 1000, "account_id": "A001"}
    account_b = {"holder": "Bob", "balance": 500, "account_id": "B001"}
    transaction_history = load_transaction_history()

    print(deposits(account_a, 200))
    record_transaction(account_a['account_id'], "Deposit", 200, transaction_history)

    print(withdraw(account_a, 150))
    record_transaction(account_a['account_id'], "Withdraw", 150, transaction_history)

    print(transfer_funds(account_a, account_b, 300))
    record_transaction(account_a['account_id'], "Transfer Out", 300, transaction_history)
    record_transaction(account_b['account_id'], "Transfer In", 300, transaction_history)


    print("Transaction History:", transaction_history)
   