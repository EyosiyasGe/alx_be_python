Monthly_income = int (input('Enter your monthly income: '))
Monthly_expense = int (input('Enter your total monthly expenses: '))
Monthly_saving = Monthly_income - monthly_expense 
Projected_savings = Monthly_saving * 12 + (Monthly_saving * 12 * 5/100 )
print ('Your monthly savings are $',Monthly_saving)
print('Projected savings after one year, with interest, is: $', Projected_savings)
