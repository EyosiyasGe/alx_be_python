from datetime import datetime,timedelta
def display_current_datetime() :
    current_date  = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date():
    
    days_to_add = timedelta(int(input("Enter the number of days to add to the current date: ")))
    current_date = datetime.now()
    future_date = current_date + days_to_add
    print(future_date.strftime("%Y-%m-%d"))
display_current_datetime()
calculate_future_date()