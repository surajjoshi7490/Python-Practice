#  Get all fruits that do NOT contain the letter "a"
fruits=['apple','cherry', 'kiwi','banana']

find_a=[char for char in fruits if not "a" in char]
print(find_a)