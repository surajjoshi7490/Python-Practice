num1 =int(input("Enter your Frist number "))
num2=int(input("Enter yout Decond number "))

operation = str(input(
"Enter \"sum\" is operation is Addition \n" 
"Enter \"sub\" is operation is Subtration \n" 
"Enter \"mul\" is operation is Multiplication \n" 
"Enter \"div\" is operation is Division \n "))

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

if operation == "sum" :
    print (sum)
elif operation == "sub":
    print (sub)
elif operation == "mul" :
    print (mul)
elif operation == "div": 
    print(div)