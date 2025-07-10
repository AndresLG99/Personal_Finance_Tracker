import pandas as pd
import matplotlib.pyplot as plt
import os

# Monthly Spending Trend
def monthly_spending_trend(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Amount"] = df["Amount"].astype(float)
    df["Month"] = df["Date"].dt.to_period("M")

    monthly_spending = df.groupby(["Month"])["Amount"].sum()
    monthly_spending.index = monthly_spending.index.to_timestamp()

    monthly_spending.plot(kind="line", marker="o")
    plt.xlabel("Month")
    plt.ylabel("Total Spending")
    plt.title("Monthly Spending")
    plt.show()

#Spending by category
def category_spending_trend(df):
    df = df[~((df["Category"] == "Income") | (df["Description"] == "Salary"))]

    category_spending = df.groupby("Category")["Amount"].sum().sort_values()

    category_spending.plot(kind="bar",title="Spending by Category")
    plt.xticks(rotation=45)
    plt.xlabel("Total Spending")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.show()

#Percentage Distribution
def category_spending_pct(df):
    df = df[~((df["Category"] == "Income") | (df["Description"] == "Salary"))]

    category_spending_pct = df.groupby("Category")["Amount"].sum()
    category_spending_pct = category_spending_pct.abs()

    category_spending_pct.plot(kind="pie",autopct="%1.1f%%",title="Spending Distribution by Category",ylabel="")
    plt.tight_layout()
    plt.show()

