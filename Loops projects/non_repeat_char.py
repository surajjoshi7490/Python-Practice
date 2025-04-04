# Given a string, find the first non-repeated character.
string="surajsura"

for i in string:
    print(i)
    if string.count(i)==1:
        print("Char is: ", i)
        break