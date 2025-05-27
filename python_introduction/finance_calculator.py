monthly_income = float (input('Enter your monthly income: '))
monthly_expense = float (input('Enter your total monthly expenses: '))
monthly_saving = monthly_income - monthly_expense 
Projected_savings = monthly_saving * 12 + (monthly_saving * 12 * 5/100 )
print ('Your monthly savings are $',monthly_saving)
print('Projected savings after one year, with interest, is: $', Projected_savings)
