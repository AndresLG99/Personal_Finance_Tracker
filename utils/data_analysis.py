import pandas as pd

# 1. Analyze spending by category
def analyze_spending_by_category(df):
    category_summary = df.groupby('Category')['Amount'].sum().reset_index()
    print("\n--- Total Spending by Category ---")
    print(category_summary.to_string(index=False, float_format='%.2f'))
    print("----------------------------------")
    expense_total = df.loc[df['Type']=='Expense', 'Amount'].sum()
    income_total  = df.loc[df['Type']=='Income' , 'Amount'].sum()
    liquidity = income_total - expense_total
    print("Liquidity:   %.2f" % liquidity)
    print("Expense:     %.2f" % expense_total)
    print("Income:      %.2f" % income_total)
    print("")

# 2. Analyze average monthly spending
def analyze_average_monthly_spending(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_summary = (
        df
        .groupby(['Month', 'Type'])['Amount']
        .sum()
        .unstack(fill_value=0)
    )
    print("\n---- Average Monthly Spending ---")
    print("Average Monthly Expense")
    for m, row in monthly_summary.iterrows():
        m_str = m.to_timestamp().strftime('%b %Y')
        print(f"{m_str}:\t{row.get('Expense', 0):.2f}")
    print("\nAverage Monthly Income")
    for m, row in monthly_summary.iterrows():
        m_str = m.to_timestamp().strftime('%b %Y')
        print(f"{m_str}:\t{row.get('Income', 0):.2f}")
    print("")

# 3. Analyze top spending category
def analyze_top_spending_category(df):
    top_expense_by_category = (
        df[df['Type']=='Expense']
        .groupby('Category')['Amount']
        .sum()
        .sort_values(ascending=False)
    )
    top_category = top_expense_by_category.idxmax()
    top_max = top_expense_by_category.max()
    print("\n--- Top Spending Category ---")
    print(f"{top_category} with {top_max:.2f} total spending.")

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_expense = (
        df[df['Type'] == 'Expense']
        .groupby(['Month', 'Category'])['Amount']
        .sum()
    )
    print("\nMonthly Top Expense by Category")
    for mon, grp in monthly_expense.groupby(level=0):
        _, top_cat = grp.idxmax()
        top_amt = grp.max()
        label = mon.to_timestamp().strftime('%b %Y')
        print(f"{label}:\t{top_cat} with {top_amt:.2f}")
    # monthly_inc = (
    #     df[df['Type'] == 'Income']
    #     .groupby(['Month', 'Category'])['Amount']
    #     .sum()
    # )
    # print("\nMonthly Top Income by Category")
    # for mon, grp in monthly_inc.groupby(level=0):
    #     _, top_cat = grp.idxmax()
    #     top_amt = grp.max()
    #     label = mon.to_timestamp().strftime('%b %Y')
    #     print(f"{label}\t{top_cat} with {top_amt:.2f}")
    print()