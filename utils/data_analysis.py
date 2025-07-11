import pandas as pd

# 1. Analyze spending by category
def analyze_spending_by_category(df):
    category_summary = df.groupby("Category")["Amount"].sum().reset_index()
    print("\n--- Total Spending by Category ---")
    print(category_summary.to_string(index=False, float_format='%.2f'))

    expense_total = df[df["Type"] == "Expense"]["Amount"].sum()
    income_total = df[df["Type"] == "Income"]["Amount"].sum()
    liquidity = income_total - expense_total
    print("----------------------------------")
    print(f"Liquidity:    {liquidity:.2f}")
    print(f"Expense:     {expense_total:.2f}")
    print(f"Income:      {income_total:.2f}")
    print()

# 2. Analyze average monthly spending
def analyze_average_monthly_spending(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

    expense_df = df[df["Type"] == "Expense"]
    income_df = df[df["Type"] == "Income"]

    # Average monthly
    # Sum per months
    monthly_expenses = expense_df.groupby("Month")["Amount"].sum()
    monthly_income = income_df.groupby("Month")["Amount"].sum()

    # List all existing month and unique
    all_months = sorted(df["Month"].unique())

    # Fill missing month value with 0
    monthly_expenses = monthly_expenses.reindex(all_months, fill_value=0)
    monthly_income = monthly_income.reindex(all_months, fill_value=0)

    # Average month with round two decimal
    average_expense = monthly_expenses.mean().round(2)
    average_income = monthly_income.mean().round(2)

    print("\n---- Average Monthly Expense ---")
    print(f"{average_expense:.2f}")
    print("\n---- Average Monthly Income ---")
    print(f"{average_income:.2f}")

    # Average per month
    # Sum per month, count, and average
    expense_stats = expense_df.groupby("Month")["Amount"].agg(sum="sum", count="count")
    expense_stats["avg_expense"] = (expense_stats["sum"] / expense_stats["count"]).round(2)
    income_stats = income_df.groupby("Month")["Amount"].agg(sum="sum", count="count")
    income_stats["avg_income"] = (income_stats["sum"] / income_stats["count"]).round(2)

    # List all existing month and unique
    all_months = sorted(df["Month"].unique())

    print("\n--- Average Expense and Income per Month ---")
    print(f"{"Month":<12} {"Avg Expense":>12} {"Avg Income":>12}")
    for m in all_months:
        label = m.to_timestamp().strftime("%b %Y")
        avg_exp = expense_stats.loc[
            m, "avg_expense"] if m in expense_stats.index else 0.00
        avg_inc = income_stats.loc[
            m, "avg_income"] if m in income_stats.index else 0.00
        print(f"{label:<12} {avg_exp:>10.2f} {avg_inc:>10.2f}")
    print()

# 3. Analyze top spending category
def analyze_top_spending_category(df):
    top_expense_by_category = (
        df[df["Type"]=="Expense"]
        .groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    top_category = top_expense_by_category.idxmax()
    top_max = top_expense_by_category.max()
    print("\n--- Top Spending Category ---")
    print(f"{top_category} with {top_max:.2f} total spending.")

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    monthly_expense = (
        df[df["Type"] == "Expense"]
        .groupby(["Month", "Category"])["Amount"]
        .sum()
    )
    print("\nMonthly Top Expense by Category")
    for mon, grp in monthly_expense.groupby(level=0):
        top_cat = grp.sort_values(ascending=False).index[0][1]
        top_amt = grp.max()
        label = mon.to_timestamp().strftime('%b %Y')
        print(f"{label:<12} {top_cat:<12} {top_amt:>10.2f}")
    print()