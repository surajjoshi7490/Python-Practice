# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number=int(input("Enter a number"))

for i in range(0,number+1):
    if i ==5:
        continue
    else:
        print(f"{number} * {i} = {number * i}")