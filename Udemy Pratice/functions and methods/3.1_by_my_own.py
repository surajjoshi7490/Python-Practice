#  Count All Characters (letters, digits, spaces, symbols)
from collections import Counter
def what_is_it(s):
    letter=digit=space=symbol=0
    for i in s:
        if i.isalpha():
            letter+=1
        elif i.isdigit():
            digit+=1
        elif i.isspace():
            space+=1
        else:
            symbol= symbol+1
    print(f"Letters: {letter}, Digits: {digit}, Spaces: {space}, Symbols: {symbol}")


s=" Hello World! 123 @#$"
what_is_it(s)

