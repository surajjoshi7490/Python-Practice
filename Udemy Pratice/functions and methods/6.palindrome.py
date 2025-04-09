def palindrome(s):
    s=s.replace(" ","").lower()
    reverse_string=s[::-1]
    if s==reverse_string:
        print("Yes this is a palindrome string")
    else:
        print("No , It's not a palindrome string")

palindrome("helleh")