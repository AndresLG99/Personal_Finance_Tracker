options = ["Open & Save Transactions",
           "Show",
           "Edit",
           "Analyze",
           "Visualize",
           "Exit"]

csv_manipulation = ["Open saved transactions",
                    "Save transactions"]

show = ["View all transactions",
        "View transactions by date range"]

edit = ["Add a new transaction",
        "Edit an existing transaction",
        "Delete an existing transaction",]

analyze = ["Analyze spending by category",
           "Calculate average monthly spending",
           "Show top spending category"]

visualize = ["Monthly spending trend",
             "Spending by category",
             "Spending percentage distribution"]

def display_menu():
    print("=" * 20 + " MAIN MENU " + "=" * 20)
    for option_index in range(len(options)):
        print(f"{option_index + 1}. {options[option_index]}")

def display_second_tier_menu(choice):
    if choice == 1:
        print("-" * 20 + " CSV Manipulation " + "-" * 20)
        for option_index in range(len(csv_manipulation)):
            print(f"{option_index + 1}. {csv_manipulation[option_index]}")
    elif choice == 2:
        print("-" * 20 + " Show " + "-" * 20)
        for option_index in range(len(show)):
            print(f"{option_index + 1}. {show[option_index]}")
    elif choice == 3:
        print("-" * 20 + " Edit " + "-" * 20)
        for option_index in range(len(edit)):
            print(f"{option_index + 1}. {edit[option_index]}")
    elif choice == 4:
        print("-" * 20 + " Analyze " + "-" * 20)
        for option_index in range(len(analyze)):
            print(f"{option_index + 1}. {analyze[option_index]}")
    elif choice == 5:
        print("-" * 20 + " Visualize " + "-" * 20)
        for option_index in range(len(visualize)):
            print(f"{option_index + 1}. {visualize[option_index]}")
    elif choice == 6:
        print("=" * 20 + " SEE YOU LATER " + "=" * 20)

def main_menu_choice():
    display_menu()
    choice = input("Enter your choice: ")

    while not choice.isdigit():
        print("Please enter a valid option.")
        choice = input("Enter your choice: ")
    while int(choice) not in range(len(options) + 1):
        print("Please enter a valid option.")
        choice = input("Enter your choice: ")

    return int(choice)

def second_tier_menu_choice(first_choice):
    choice = input("Enter your choice: ")

    while not choice.isdigit():
        print("Please enter a valid option.")
        choice = input("Enter your choice: ")
    if first_choice == 1:
        while int(choice) not in range(len(csv_manipulation) + 1):
            print("Please enter a valid option.")
            choice = input("Enter your choice: ")
    elif first_choice == 2:
        while int(choice) not in range(len(show) + 1):
            print("Please enter a valid option.")
            choice = input("Enter your choice: ")
    elif first_choice == 3:
        while int(choice) not in range(len(edit) + 1):
            print("Please enter a valid option.")
            choice = input("Enter your choice: ")
    elif first_choice == 4:
        while int(choice) not in range(len(analyze) + 1):
            print("Please enter a valid option.")
            choice = input("Enter your choice: ")
    elif first_choice == 5:
        while int(choice) not in range(len(visualize) + 1):
            print("Please enter a valid option.")
            choice = input("Enter your choice: ")

    return int(choice)

x = main_menu_choice()
display_second_tier_menu(x)
second_tier_menu_choice(x)