st = 'Print only the words that start with s in this sentence'

count=[char for char in st.split() if char[0]=="s" in char]
print(count)