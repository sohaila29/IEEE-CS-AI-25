def leep_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def days_in_month(month, year):
    if month ==2:
        return 29
    elif month ==2 and leep_year(year):
        return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30
    

def next_week(day, month, year):
    day += 7

    days_this_month = days_in_month(month, year)
    if day > days_this_month:
        day -=days_this_month

        month += 1
        if month > 12:
            month = 1
            year +=1
    return day, month, year


day = int(input("enter day:"))
month = int(input("enter month:"))
year = int(input("enter year:"))
day2,month2,year2 =next_week(day, month, year)  
print(f"Day: {day2} Month:{month2} Year:{year2}")