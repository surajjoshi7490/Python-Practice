# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald():
    Name=str(input("Enter a name :-"))
    return Name[0].upper()+Name[1:3]+Name[3].upper()+Name[4:]

print(old_macdonald())