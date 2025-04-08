lists=[1,2,4,0,0,7,5]

code=[0,0,7]
for num in lists:
    if num==code[0]:
        code.pop(0)
        if not code:
            print (True)
            break
else:
         print(False)  

