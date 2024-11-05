import pandas as pd
from datetime import datetime

# Function to parse the date string
def parse_date(date_str):
    # Try parsing the date with different formats
    for fmt in ("%d-%m-%Y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    # If none of the formats match, raise an error
    raise ValueError("Date format is incorrect. Please use DD-MM-YYYY format.")

# Function to add a new entry to the finance_data.csv file
def add_entry(date, income, expense, description):
    try:
        # Parse and reformat the date
        date_obj = parse_date(date)
        formatted_date = date_obj.strftime("%d-%m-%Y")  # Convert date to "DD-MM-YYYY" format
    except ValueError as e:
        print(e)
        return
    
    # Create a dictionary for the new entry
    new_data = {
        "Date": formatted_date,
        "Income": income,
        "Expense": expense,
        "Description": description
    }

    # Read existing data, if any, from finance_data.csv
    try:
        df = pd.read_csv('finance_data.csv')
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame with specified columns
        df = pd.DataFrame(columns=["Date", "Income", "Expense", "Description"])

    # Append the new data
    df = pd.concat(new_data, ignore_index=True)
    
    # Save back to CSV
    df.to_csv('finance_data.csv', index=False)
    print("Data entry added successfully.")

# Example usage
if __name__ == "__main__":
    # Prompt user for data entry
    date = input("Enter the date (DD-MM-YYYY): ")
    income = float(input("Enter the income: "))
    expense = float(input("Enter the expense: "))
    description = input("Enter a description: ")
    
    # Add entry to the CSV
    add_entry(date, income, expense, description)
