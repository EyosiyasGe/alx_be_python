import datetime
def display_current_datetime() :
    current_date  = datetime.datetime.now()
    return current_date 
print(display_current_datetime())
def calculate_future_date():
    days_to_add = datetime.timedelta(int(input('Enter the number of days: ')))
    current_date = datetime.datetime.now()
    future_date = current_date + days_to_add
    return future_date
display_current_datetime()
print(calculate_future_date())