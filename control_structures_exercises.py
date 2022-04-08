#1) Conditional Basics

#A)prompt the user for a day of the week, print out whether the day is Monday or not

day = input("day_of_the_week?")
if day == "Monday":
print("Happy Monday")
else: 
print("Today is not Monday")

#B)prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekend = ["Saturday", "Sunday"]

day = input("day_of_the_week?")

if day not in weekend:
    print("Today is a Weekday")
else:
    print("Today is The Weekend")

#C)create variables and make up values for
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be

#write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
hr = input("Hours Worked? ")
hr = int(hr)
rate = input("hourly Rate? ")
rate = int(rate)
week_pay = hr * rate
if hr > 40:
    print((rate * 40)+(1.5 * rate * (hr - 40)))
else:
    print(week_pay)