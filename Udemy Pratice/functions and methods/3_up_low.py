# def up_low(s):
#     no_upper=0
#     no_lower=0
#     for i in s:
#         if i.isupper():
#             no_upper+=1
            
#         elif i.islower():
#             no_lower+=1
#     print(f"Expected Output:\nNo. of Upper case char: {no_upper}\nNo. of Lowercase char : {no_lower}")
# s='Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)
from collections import Counter

def up_low(s):
    count=Counter({'upper':0,'lower':0})
    for i in s :
        if i.isupper():
            count['upper']+= 1
        elif i.islower():
            count['lower']+=1
    print(f"Expected Output:\nNo. of Upper case char: {count['upper']}\nNo. of Lowercase char : {count['lower']}")
 
s='Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)