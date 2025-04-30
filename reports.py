#Reports
#Use panda to reports from the accounts
import pandas as pd

def create_balance_report(accounts_data):
    if not accounts_data:
        print("No accounts found to generate a report.")
        return

    # Convert accounts_data dictionary into a Pandas DataFrame
    df = pd.DataFrame.from_dict(accounts_data, orient="index")

    # Rename columns for better readability  
    df = df.rename(columns={
        "holder": "Holder Name",
        "account_type": "Account Type",
        "balance": "Balance"
    })

    # Reset the index to include Account ID as a column
    df.reset_index(inplace=True)
    df.rename(columns={"index": "Account ID"}, inplace=True)

    # Print the report
    print("\nBalance Report:")
    print(df.to_string(index=False))

    #save the report to a CSV file
    df.to_csv("balance_report.csv", index=False)
    print("\nReport saved to 'balance_report.csv'.")
