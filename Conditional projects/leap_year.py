# Determine if a year is a leap year

year=int(input("Enter a year you wants to check for leap year"))

if (year%4==0 and year%100!=0) or year%400==0 :
    print("yes its a leap year")
