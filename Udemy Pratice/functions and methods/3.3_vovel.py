from collections import Counter
strings="Count Vowels and Consonants"
vovels="aeiouAEIOU"
v=c=0
for i in strings:
    if i.isalpha():
        if i in vovels:
            v+=1
        else:
            c+=1
print(f"there are {v}Vovels and {c}Consonants")