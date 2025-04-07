def almost_there():
    number=int(input("Enter a number"))
    if abs(100-number)<=10 or abs(200-number)<=10:
        return True
    else :
        return False

print(almost_there())