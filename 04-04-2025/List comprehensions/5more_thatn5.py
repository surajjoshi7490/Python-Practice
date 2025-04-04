# Get fruits that have more than 5 letters

fruits=['apple','cherry', 'kiwi','banana']
length_of_chr=[ len(char)>5 for char in fruits]

print(length_of_chr)