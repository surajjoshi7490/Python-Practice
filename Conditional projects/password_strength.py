# Check if a password is "Weak", "Medium", or "Strong". Criteria: 
# < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password=str(input("Enter you password"))

if len(password) < 6 :
    print("your password is weak")
elif 6<=len(password)<=10:
    print("Your password is good ")
else :
    print("your password is storng")