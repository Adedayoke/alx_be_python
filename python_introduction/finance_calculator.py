# finance_calculator.py
# Personal Finance Calculator
# This program calculates monthly savings and projects annual savings with interest

# User input for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest rate
# Using the formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")