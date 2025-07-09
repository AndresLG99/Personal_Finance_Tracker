# IMPORTS
import pandas as pd
import os
from _datetime import datetime

# INITIAL DATA STRUCTURES AND VARIABLES
main_menu_options = ["Import",
                     "Show",
                     "Modify",
                     "Analyze",
                     "Visualize",
                     "Budget",
                     "Save",
                     "Exit"]

show_menu_options = ["View all transactions",
                     "View transactions by date range"]

modify_menu_options = ["Add a transaction",
                       "Edit a transaction",
                       "Delete a transaction"]

analyze_menu_options = ["Analyze spending by category",
                         "Analyze average monthly spending",
                         "Analyze top spending category"]

visualize_menu_options = ["Monthly spending trend",
                          "Spending by category",
                          "Percentage distribution"]

current_path = os.path.abspath(__file__)
base_dir = os.path.dirname(os.path.dirname(current_path))
directory = os.path.join(base_dir, "data")

# FUNCTIONS
def display_menu(menu):
    for index, option in enumerate(menu):
        print(f"{index + 1}. {option}")

def display_files():
    files_list = []
    for index, file in enumerate(os.listdir(directory)):
        if os.path.isfile(os.path.join(directory, file)):
            files_list.append(file)
            print(f"{index + 1}. {file}")
    return files_list

def open_csv(filename):
    df = pd.read_csv(f"{directory}\\{filename}", parse_dates=["Date"])
    print("File loaded successfully!")
    return df

def show_all_transactions(df):
    print(df)

def show_filtered_transactions(df, init_date, end_date):
    df2 = df[df["Date"] >= init_date]
    df3 = df2[df2["Date"] <= end_date]
    print(df3)

def add_transaction(df, param1, param2, param3, param4, param5):
    new_transaction = {"Date": param1,
                       "Category": param2,
                       "Description": param3,
                       "Amount": param4,
                       "Type": param5}
    df_new = df.loc[len(df)] = new_transaction
    print("New transaction added successfully!")
    return df_new

def edit_transaction(df, row_index, column_name, new_value):
    df.loc[row_index, column_name] = new_value
    print("Transaction edited successfully!")
    return df

def delete_transaction(df, index):
    df = df.drop([index, index])
    print("Transaction deleted successfully!")
    return df

def save_csv(df, filename):
    df.to_csv(f"{directory}\\{filename}", index=False)
    print("File saved successfully!")

def ask_date():
    while True:
        user_input = input("Enter the Date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(user_input, "%Y-%m-%d")
            return date.date()
        except ValueError:
            print("Invalid date format. Please try again.")

def ask_params():
    param1 = ask_date()
    param2 = input("Enter the Category: ")
    param3 = input("Enter the Description: ")
    param4 = input("Enter the Amount: ")
    param5 = input("Enter the Type: ")
    return param1, param2, param3, param4, param5

def row_index_list(df):
    print("\nPlease choose a row index.\n")
    index_list = df.index.tolist()
    print(df)
    return index_list

def column_name_list(df):
    column_list = df.columns.tolist()
    for i, item in enumerate(column_list):
        print(f"{i + 1}. {item}")
    return column_list

def ask_new_value(column):
    if column == 1: #Date
        new_value = ask_date()
    elif column == 2: #Category
        new_value = input("Enter the new Category: ")
    elif column == 3: #Description
        new_value = input("Enter the new Description: ")
    elif column == 4: #Amount
        try:
            new_value = float(input("Enter the new Amount: "))
        except ValueError:
            print("Invalid value. Please try again.")
    elif column == 5: #Type
        new_value = input("Enter the new Type: ")
    return new_value