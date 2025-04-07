strings='surajcefgklmnjoshi'
new_string=''
skip=False
for i in strings:
    if i=='c':
        skip=True
    elif i=='n' and skip:
        skip=False
    elif not skip:
        new_string+=i

print(new_string)
