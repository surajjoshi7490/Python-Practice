''' Assign a letter grade based on a student's :
A = 90 -100
b = 80-89
c = 70-79
d = 60-69
f = below 60'''

Grade = int(input("Enter your marks "))

if 100<=Grade<=90:
    print("You have got \"A\" grade")
elif 89<=Grade<=80:
    print("You have got \"B\" grade")
elif 79<=Grade<=70:
    print("You have got \"C\" grade")
elif 69<=Grade<=60:
    print("You have got \"D\" grade")
elif Grade<60 :
    print("You have got \"E\" grade")
