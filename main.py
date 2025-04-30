#main       
#Gotta make all these files function as one
#import all the file on to here first 

from auth import register_user, login_user
from accounts import create_account, display_account_details
from transactions import deposits, withdraw, transfer_funds, load_transaction_history
from Storage import save_data, load_data, export_to_csv, export_to_txt
from reports import create_balance_report
from plotting import plot_balance_trends

#A main menu so others can choose where to explore
def main_menu():
    print("\nWelcome to this banking program.")
    print("[1] Holder Authetication.")
    print("[2] Accounts")
    print("[3] Transactions")
    print("[4] Storage")
    print("[5] Reports")
    print("[6] Visualizations")
    print("[7] Escape from here!")

#time to call all the function to help get to the others
def main():
    users_data = load_data("users.json")
    #create a few exceptions to help with json file and load transactions
    try:
        accounts_data = load_data("accounts.json")
    except FileNotFoundError:
        print("accounts.json file not found. Creating a new one.")
        accounts_data = {}
        save_data("accounts.json", accounts_data)  # Create an empty file
    try:
        transaction_history = load_transaction_history()
    except FileNotFoundError:
        print("Transaction history file not found. Starting with an empty history.")
        transaction_history = []

    #use branching to control the choices made in the main menu
    while True:
        main_menu()
        choice = input("Please choose: ").strip()

        if choice == "1":
            print("\n[Holder Authetication]")
            action = input("Select: [Register/Login]: ").strip().lower()
            if action == "register":
                username = input("Enter username: ")
                password = input("Enter password: ")
                register_user(username, password)
            elif action == "login":
                username = input("Enter username: ")
                password = input("Enter password: ")
                login_user(username, password)

            #2nd option Accounts
        elif choice == "2":
            print("\n[Accounts]")
            action = input("Select: [Create or view]: ").strip().lower()
            if action == "create":
                account_type = input("Enter account type [Savings or Checkings]: ").strip().lower()
                if account_type not in ["savings", "checkings"]:
                    print("Invalid account type. Please enter 'Savings' or 'Checkings'.")
                    return
                holder = input("Enter holder name: ")
                account_id = input("Account ID: ")
                if account_id in accounts_data:
                    print("Account ID already exists. Please choose a different ID.")
                    return
                try:
                    initial_balance = float(input("Deposit initial amount: "))
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
                    return
                account = create_account(account_type, holder, account_id, initial_balance)
                accounts_data[account_id] = account
                accounts_data[account_id] = {
                    "holder": holder,
                    "balance": initial_balance,
                    "account_type": account_type
                }
                save_data("accounts.json", accounts_data)
                print(f"Account created successfully: {accounts_data[account_id]}")

            elif action == "view":
                accounts_data = load_data("accounts.json")  # Reload the latest data
                account_id = input("Select account ID: ")
                if account_id in accounts_data:
                    display_account_details(accounts_data[account_id])
                else:
                    print("This account is not here, please try again or create an account.")

        elif choice == "3":
            print("\n[Transactions]")
            account_id = input("Input account ID: ")
            if account_id in accounts_data:
                action = input("Select action: [Deposit or Withdraw or Transfer]").strip().lower()
                if action == "deposit":
                    try:
                        amount = float(input("Deposit Amount: "))
                        deposits(accounts_data[account_id], amount)
                        save_data("accounts.json", accounts_data)  # Save changes
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                elif action == "withdraw":
                    try:
                        amount = float(input("How much are you going to pull out? "))
                        withdraw(accounts_data[account_id], amount)
                        save_data("accounts.json", accounts_data)  # Save changes
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                elif action == "transfer":
                    to_account_id = input("Enter the account ID of the receiver: ")
                    if to_account_id in accounts_data:
                        try:
                            amount = float(input("How much is being moved? "))
                            transfer_funds(accounts_data[account_id], accounts_data[to_account_id], amount)
                            save_data("accounts.json", accounts_data)  # Save changes
                        except ValueError:
                            print("Invalid input. Please enter a numeric value.")
                    else:
                        print("Receiver account ID not found.")
            else:
                print("This account is not here, please try again or create an account.")
        
        #Storage
        elif choice == "4":
            print("\n[Storage]")
            save_data("user.json", users_data)
            save_data("accounts.json", accounts_data)
            export_to_csv("transactions.csv", transaction_history)
            export_to_txt("transactions.txt", transaction_history)

        elif choice == "5":
            print("\n Reports")   
            create_balance_report(accounts_data)

        elif choice == "6":
            print("\nPlotting")
            if not transaction_history:
                print("No transaction history available to plot.")
            else:
                plot_balance_trends(transaction_history)

        elif choice == "7":
            print("Breakout of here, Goodbye!")
            break

        else:
            print("wrong choice. Please try again")    

#Run this program
if __name__ == "__main__":
    #Run the main function to start the program
  main()



