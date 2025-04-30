#File Storage
#import a json file to store data and csv
import json
import csv
#Create a function that opens file and saves data
def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data stored to {file_name}.")

#Gotta set up error management to ensure good handling of missing or corrupt files
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with empty data.")
        return{}
    except json.JSONDecodeError:
        print(f"Error decoding {file_name}. Starting with empty data")
        return {}
    
#Create a way to export CSV or TXT

def export_to_csv(file_name, transaction_history):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account ID", "Transaction Type", "Amount", "Date"])
        for transaction in transaction_history:
            writer.writerow([transaction["account_id"], transaction["type"], transaction["amount"], transaction["date"]])
    print(f"Transaction history exported to {file_name}")

#lets make one for exporting to TXT
def export_to_txt(file_name, transaction_history):
    with open(file_name, 'w') as file:
        file.write("Transaction History:\n")
        for transaction in transaction_history:
            file.write(f"Account Id: {transaction['account_id']}")
            print(f"Transaction history exported to {file_name}.")