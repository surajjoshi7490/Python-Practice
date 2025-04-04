# Calculate the sum of even numbers up to a given number n.

number=int(input("Enter a number"))
even_numbers_sum=0

for i in range(0,number+1):
    if i%2==0:
        even_numbers_sum = i + even_numbers_sum
        print(f"{even_numbers_sum} = {i}")
     
