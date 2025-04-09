# Compute the factorial of a number using a while loop. int(input("Enter your number"))

''' for 5*4*3*2*1'''
number=5 
factorial=1

while number>0:
    factorial=factorial*number # fact = 1 .. 1*5=5  , fact=5 .. so 5*4 = 20 ..., fact = 60 number=2 60*2=120
    number=number -1
    print(factorial)


'''  1*2*3*4*5 '''
# number=5 
# factorial=1
# i=1
# while i<=number:
#         factorial=i*factorial
#         print(factorial)
#         i=i+1
        