# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
items = ["apple", "banana", "orange", "apple", "mango"]

unique_items=set()

for i in items:
    if i in unique_items:
        print("got a Dublicate :" ,i)
        break
    unique_items.add(i)
    
