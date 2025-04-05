# Go through the string below and if the length of a word is even print "even!"**
st = 'Print every word in this sentence that has an even number of letters'
even=[char for char in st.split() if len(char)%2==0  ]
print(even)
