# finance_calculator.py

# طلب الدخل والمصاريف الشهرية
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# حساب الادخار الشهري
monthly_savings = monthly_income - monthly_expenses

# حساب الادخار السنوي المتوقع مع الفائدة 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# طباعة النتائج
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
