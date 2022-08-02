#Instructions:

# In the starting code, you'll find the solution from the Leap Year challenge. First, 
# convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
# it should return True if it is a leap year and return False if it is not a leap year.
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:28
# The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
        return True
      else:
        print("Not leap year.")
        return False
    else:
      print("Leap year.")
      return True
  else:
    print("Not leap year.")
    return False

def days_in_month(year_is, month_is):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leap_year_or_not = is_leap(year=year_is)
  if leap_year_or_not == True:
    month_days[1]+=1
    return month_days[month_is]
  
  else:
    return month_days[month_is]
  
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year_is=year, month_is = month)
print(days)












