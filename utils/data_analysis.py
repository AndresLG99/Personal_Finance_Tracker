# 1
def analyze_spending_by_category(df):
    cat_summary = df.groupby('Category')['Amount'].sum().reset_index()
    print("\n--- Total spending by Category ---")
    print(cat_summary.to_string(index=False, float_format='%.2f'))
    print("----------------------")
    print("Total\t%.2f" % cat_summary['Amount'].sum())
    expense_total = df.loc[df['Type']=='Expense', 'Amount'].sum()
    income_total  = df.loc[df['Type']=='Income' , 'Amount'].sum()
    print("\tExpense: %.2f" % expense_total)
    print("\tIncome:  %.2f" % income_total)