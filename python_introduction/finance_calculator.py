income = int (input('Enter your monthly income: '))
expense = int (input('Enter your total monthly expenses: '))
saving = income - expense 
annual_saving = saving * 12 + ( saving * 12 * 0.05 )
print ('Your monthly savings are $',saving)
print('Projected savings after one year, with interest, is: $', annual_saving)
