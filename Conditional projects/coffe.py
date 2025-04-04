# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
size = str(input("Enter which size of coffe you want  : "))

extra=str(input("if you want a Extra Shot of Espresso press :  1  else  :0"))

if extra ==1 :
    print(f"Your {size.upper()}coffe is redy with a Extra Shot of Espresso ")
else :
    print(f"Your {size.upper()} Coffe is redy")