# classify a person's age group :
#  child < 13 , Teenager 13 - 19 , Adult 20 - 59 , Senior 60+

age = int(input("Enter your age "))

if age < 13 :
    print("You are a child")
elif 13<=age<=19 :
    print("Your are a Teenager")
elif 20<=age<=59:
    print("You are a Adult ")
elif age >=60:
    print("You are a Senior ")

