task = input("Enter your task: ")
priority = input ("Priority (high/medium/low): ")
time_bound = input ("Is it time-bound? (yes/no): ")
match priority :
    case "high" :
        if time_bound=="yes" and priority == "high":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound=="no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else :
            print("try again")
    case _:
        print ( "enter valid time bound")