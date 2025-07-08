# IMPORTS
import pandas as pd
from utils.menu import *
from utils.import_save_csv import *
import os

# FUNCTIONS
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# INITIAL DATA STRUCTURES AND VARIABLES
user_name = input("Enter your name: ")
clear_console()
print(f"Welcome {user_name}.")
df = open_csv()

# MAIN STRUCTURE
x = main_menu_choice()
display_second_tier_menu(x)
y = second_tier_menu_choice(x)