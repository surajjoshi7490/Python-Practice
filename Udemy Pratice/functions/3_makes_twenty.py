def is_twenty():
    n1=int(input("First Number :- "))
    n2=int(input("Second Number :- "))
    # if a+b==20 or a==20 or b==20:
    #     return True
    # else:
    #     return False
    return (n1+n2)==20 or n1==20 or n2==20
print(is_twenty())