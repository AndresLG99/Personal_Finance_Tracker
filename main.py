# IMPORTS
import os
from utils.data_management import *
from utils.data_analysis import *

# INITIAL DATA STRUCTURES AND VARIABLES
on_off = True

# FUNCTIONS
def clear_console():
    return os.system('cls' if os.name == 'nt' else 'clear')

def user_name():
    name = input("Enter your name: ")
    return name

def ask_choice(menu):
    choice = input("Enter your choice: ")
    while not choice.isdigit() or int(choice) not in range(len(menu) + 1):
        print("Please enter a valid choice.")
        choice = input("Enter your choice: ")
    return int(choice)

def next_menu():
    option_list = ["yes", "no"]
    option = input("Continue? (yes/no): ").lower()
    while option not in option_list:
        print("Please enter a valid choice.")
        option = input("Continue? (yes/no): ").lower()
    return option

def ask_initial_date():
    while True:
        initial_date = input("Enter the Initial Date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(initial_date, "%Y-%m-%d")
            date = date.date()
            return date.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")

def ask_end_date():
    while True:
        end_date = input("Enter the End Date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(end_date, "%Y-%m-%d")
            date = date.date()
            return date.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")

# MAIN STRUCTURE
user_name = user_name()
print(f"Welcome to your Personal Finance Tracker {user_name.capitalize()}")

while on_off:
    print("=" * 20 + " MAIN MENU " + "=" * 20)
    display_menu(main_menu_options)
    first_choice = ask_choice(main_menu_options)

    if first_choice == 1:
        print("-" * 20 + " Available Files " + "-" * 20)
        files_list = display_files()
        file_choice = ask_choice(files_list)
        dataframe = open_csv(files_list[file_choice - 1])
        while next_menu() == "no":
            pass
        clear_console()

    elif first_choice == 2:
        print("-" * 20 + " Show Menu " + "-" * 20)
        display_menu(show_menu_options)
        show_choice = ask_choice(show_menu_options)

        if show_choice == 1:
            try:
                show_all_transactions(dataframe)
            except NameError:
                print("\nYou haven't chosen any file yet.")

        elif show_choice == 2:
            first_date = ask_initial_date()
            second_date = ask_end_date()
            try:
                show_filtered_transactions(dataframe,first_date,second_date)
            except NameError:
                print("\nYou haven't chosen any file yet.")

        while next_menu() == "no":
            pass
        clear_console()

    elif first_choice == 3:
        print("-" * 20 + " Modify Menu " + "-" * 20)
        display_menu(modify_menu_options)
        modify_choice = ask_choice(modify_menu_options)
        if modify_choice == 1:
            try:
                x, y, z, a, b = ask_params()
                add_transaction(dataframe, x, y, z, a, b)
            except NameError:
                print("\nYou haven't chosen any file yet.")
        elif modify_choice == 2:
            try:
                index_list = row_index_list(dataframe)
                row_choice = ask_choice(index_list)
                column_list = column_name_list(dataframe)
                column_choice = ask_choice(column_list)
                new_value = ask_new_value(column_choice)
                edit_transaction(dataframe,row_choice,column_list[column_choice - 1],new_value)
            except NameError:
                print("\nYou haven't chosen any file yet.")
        elif modify_choice == 3:
            index_list2 = row_index_list(dataframe)
            row_choice2 = ask_choice(index_list2)
            dataframe = delete_transaction(dataframe,row_choice2)
        while next_menu() == "no":
            pass
        clear_console()

    elif first_choice == 4:
        print("-" * 20 + " Analyze Menu " + "-" * 20)
        display_menu(analyze_menu_options)
        analyze_choice = ask_choice(analyze_menu_options)
        # MISSING CODE
        if analyze_choice == 1:
            try:
                analyze_spending_by_category(dataframe)
            except NameError:
                print("\nYou haven't chosen any file yet.")
        while next_menu() == "no":
            pass
        clear_console()

    elif first_choice == 5:
        pass

    elif first_choice == 6:
        print("-" * 20 + " Available Files " + "-" * 20)
        files_list = display_files()
        file_choice = ask_choice(files_list)
        save_csv(dataframe,files_list[file_choice - 1])
        while next_menu() == "no":
            pass
        clear_console()

    elif first_choice == 7:
        on_off = False
        clear_console()
        print()
        print("=" * 20 + " THANK YOU " + "=" * 20)
