# IMPORTS
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# INITIAL DATA STRUCTURES AND VARIABLES
budget_menu_options = ["Set category budget",
                       "Check budget status",
                       "Visualize spending trends"]

visualize_budget_menu_options = ["Monthly income vs. spending",
                                 "Category spending vs. budget",
                                 "Income & expense distribution"]

# FUNCTIONS
def income_vs_expense_graph(df):
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_totals = df.groupby(["Month", "Type"])["Amount"].sum().unstack(fill_value=0)
    monthly_totals.plot(kind='line', marker='o', figsize=(10, 6))
    plt.title("Monthly Income vs Expense")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.grid(True)
    plt.legend(title="Type")
    plt.tight_layout()
    plt.show()

def set_cat_budget(df):
    unique_categories = df["Category"].unique()
    budget_list = []
    while True:
        try:
            for i in unique_categories:
                val = float(input(f"Enter your monthly budget for {i}: $"))
                budget_list.append(val)
            return budget_list
        except ValueError:
            print("Please enter a number.")

def show_budgets(df, budget_list):
    print("\nHere is your budget by category")
    unique_categories = df["Category"].unique()
    for i, item in enumerate(unique_categories):
        print(f"{i + 1}. {item}: ${budget_list[i]}")

def income_vs_expense_totals(df):
    totals = df.groupby("Type")["Amount"].sum()
    total_income = totals.get("Income", 0)
    total_expense = totals.get("Expense", 0)
    return total_income, total_expense

def income_vs_expense_cats(df):
    totals = df.groupby("Category")["Amount"].sum()
    spent_by_cat_list = []
    unique_categories = df["Category"].unique()
    for item in unique_categories:
        val = totals.get(item, 0)
        spent_by_cat_list.append(float(val))
    return spent_by_cat_list

def show_i_v_e_cats(df, cats_list):
    print("\nHere is your summary of transactions by category")
    unique_categories = df["Category"].unique()
    for i, item in enumerate(unique_categories):
        print(f"{i + 1}. {item}: ${cats_list[i]}")

def show_budget_vs_real(df,list1, list2):
    print("\nHere is your budget vs real transactions")
    unique_categories = df["Category"].unique()

    for i, item in enumerate(unique_categories):
        print(f"{i + 1}. {item}:\nBudget: ${list1[i]} | Real: ${list2[i]}")

        if list1[i] * 0.8 <= list2[i] < list1[i]:
            print("WARNING: You are over 80% of the budget.\n")

        elif list2[i] >= list1[i]:
            print("URGENT: You have reached the budget.\n")

        else:
            print("HEALTHY: You are under 80% of the budget.\n")

    x, y = income_vs_expense_totals(df)
    print(f"Overall:\nIncome: ${x} | Expense: ${y}")
    if x < y:
        print(f"ALERT: You have spent {round(((y - x) / y) * 100, 2)}% more than you have earned.")
    else:
        print(f"HEALTHY: You have spent {round(((x - y) / x) * 100, 2)}% less than you have earned.")

def budget_vs_real_graph(df, list1, list2):
    unique_categories = df["Category"].unique()
    x = np.arange(len(unique_categories))
    width = 0.35
    plt.figure(figsize=(10, 6))
    plt.bar(x - width / 2, list1, width, label="Budget")
    plt.bar(x + width / 2, list2, width, label="Real")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Budget vs Real Transactions")
    plt.xticks(x, unique_categories, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def percentage_distribution_graph(df, list1):
    unique_categories = df["Category"].unique()
    plt.figure(figsize=(6, 6))
    plt.pie(list1, labels=unique_categories, autopct='%1.1f%%', startangle=140)
    plt.title("Percentage Distribution by Category")
    plt.axis("Equal")
    plt.show()
