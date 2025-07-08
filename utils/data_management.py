# IMPORTS
import pandas as pd
import os

# INITIAL DATA STRUCTURES AND VARIABLES
main_menu_options = ["Import",
                     "Show",
                     "Modify",
                     "Analyze",
                     "Visualize",
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
    df = pd.read_csv(f"{directory}\\{filename}")
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
    df.append(new_transaction)
    return df

def edit_transaction(df, row, column, new_value):
    df.loc[row, column] = new_value
    return df

def delete_transaction(df, index):
    df = df.drop([index, index + 1])
    return df

def save_csv(df, filename):
    df.to_csv(filename, index=False)
    print("File saved successfully!")
