''' movie ticket are priced based on age :
if age is 18 or more price is 12$ 
if age is less than 18 price is 8$
if today is wednesday get discount of 2$ '''

age = int(input("Enter your age : "))
day=str(input("Enter wed is today is WEDNESDAY : "))

price = 12 if age>18 else 8

if day== "wed":
    print(f"{price-2}$")
else :
    print(f"{price}$")

