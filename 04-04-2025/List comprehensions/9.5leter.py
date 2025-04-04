# Get a list of fruits that have exactly 5 letters, in uppercase

fruits=['apple','cherry', 'kiwi','banana','grape']

letters=[ char.upper() for char in fruits if len(char)==5 ]
print(letters)