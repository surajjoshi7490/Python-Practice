# Count how many fruits have the letter "e"
fruits=['apple','cherry', 'kiwi','banana']

e_letter=len([ char for char in fruits if "e" in char])
print(e_letter)