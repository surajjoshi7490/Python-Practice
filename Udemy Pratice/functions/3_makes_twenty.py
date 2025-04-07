def is_twenty():
    a=int(input("First Number :- "))
    b=int(input("Second Number :- "))
    if a+b==20 or a==20 or b==20:
        return True
    else:
        return False
    
print(is_twenty())