from collections import Counter

def using_counter(s):
    word=s.split()
    used_counter=Counter(word)
    return used_counter
print(using_counter("This is a new type is this a type"))