import pandas as pd
from datetime import datetime, timedelta
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to read data from a CSV file
def read_data(file_path):
    data = pd.read_csv(file_path)
    # Convert 'order_date' column to datetime format with specified format
    data['order_date'] = pd.to_datetime(data['order_date'], format='%m/%d/%Y')
    return data

# Function to predict the next order date and quantity
def predict_next_order(dates, quantities):
    # Calculate the differences between order dates
    diffs = dates.diff().dropna()
    
    # Calculate the average interval between orders
    mean_diff = diffs.mean()
    
    # Calculate the next order date
    last_order_date = dates.max()
    next_order_date = last_order_date + mean_diff
    
    # Ensure the next order date is not already in the dates
    while next_order_date in dates.values:
        next_order_date += mean_diff
    
    # Calculate the average quantity of products and round to the nearest integer
    mean_quantity = round(quantities.mean())
    
    # Calculate the total value of the next order
    next_order_value = mean_quantity * 2
    
    return next_order_date, mean_quantity, next_order_value

# Function to handle predictions for a selected customer
def handle_prediction(data):
    # Get the unique customer IDs
    customer_ids = data['customer_id'].unique()
    
    # Print available customers
    print("Available customers:")
    for customer_id in customer_ids:
        print(f"Customer ID: {customer_id}")
    
    # Ask user to select a customer
    selected_customer_id = int(input("Enter the Customer ID you want the prediction for: "))
    
    if selected_customer_id not in customer_ids:
        print("Invalid Customer ID.")
        return
    
    # Filter the data for the selected customer
    group = data[data['customer_id'] == selected_customer_id]
    group = group.sort_values(by='order_date')
    
    # Predict the next order for the selected customer
    next_order_date, mean_quantity, next_order_value = predict_next_order(group['order_date'], group['quantity'])
    
    # Print the result
    print(f'Customer {selected_customer_id}:')
    print(f'  The next order is expected on: {next_order_date.strftime("%Y-%m-%d")}')
    print(f'  Average quantity of products: {mean_quantity}')
    print(f'  Total value of the next order: ${next_order_value:.2f}')

# Main function
def main():
    data = None
    while True:
        if data is None:
            # Open a file dialog to select the CSV file
            Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
            file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])  # Show an "Open" dialog box and return the path to the selected file
            
            if not file_path:
                print("No file selected.")
                return
            
            # Read the data
            data = read_data(file_path)
        
        # Handle the prediction
        handle_prediction(data)
        
        # Ask user if they want to make another prediction or exit
        choice = input("Do you want to make another prediction or exit? (1- Another Prediction, 2- Exit): ")
        if choice == '2':
            break
        elif choice == '1':
            # Ask if user wants to use the same data or load new data
            data_choice = input("Do you want to use the same data or load a new data source? (1- Same Data, 2- New Data): ")
            if data_choice == '2':
                data = None  # This will trigger loading new data in the next iteration

if __name__ == "__main__":
    main()
