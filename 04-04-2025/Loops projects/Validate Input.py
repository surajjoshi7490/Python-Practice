#  Keep asking the user for input until they enter a number between 1 and 10.

while True:
    user=int(input("enter a number between 1-10"))
    if 1<=user<=10:
        print("Thanks")
        break
    else:
        print("try again")
