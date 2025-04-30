# Plotting
# Use NumPy, Pandas, and MatplotLib to plot the data
import matplotlib.pyplot as plt
import pandas as pd

def plot_balance_trends(transaction_history):
    if not transaction_history:
        print("No transaction history available to plot.")
        return

    # Convert transaction history to a Pandas DataFrame
    df = pd.DataFrame(transaction_history)

   
    if "timestamp" not in df.columns or "balance" not in df.columns:
        print("Transaction history is missing required fields ('timestamp' or 'balance').")
        return

    
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    
    df = df.sort_values(by="timestamp")

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(df["timestamp"], df["balance"], marker="o", linestyle="-", color="b")
    plt.title("Balance Trends Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Balance")
    plt.grid(True)
    plt.xticks(rotation=45)  
    plt.tight_layout()  
    plt.show()

    