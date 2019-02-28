"""
1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"
"""
#num = 1

def whatday(num):
    day_in_week_number = num
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Wrong, please enter a number between 1 and 7']
    if day_in_week_number == 1:
        return(days_of_week[int(day_in_week_number - 1)])
    elif day_in_week_number == 2:
        return(days_of_week[int(day_in_week_number - 1)])
    elif day_in_week_number == 3:
        return(days_of_week[int(day_in_week_number - 1)])
    elif day_in_week_number == 4:
        return(days_of_week[int(day_in_week_number - 1)])
    elif day_in_week_number == 5:
        return(days_of_week[int(day_in_week_number - 1)])
    elif day_in_week_number == 6:
        return(days_of_week[int(day_in_week_number - 1)])
    elif day_in_week_number == 7:
        return(days_of_week[int(day_in_week_number - 1)])
    else:
        return(days_of_week[7])

#print(whatday(num))