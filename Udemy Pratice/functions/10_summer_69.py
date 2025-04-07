lists=(1,2,5,6,8,2,9,8)
skip = False
result=0
for i in lists:
    if i==6 :
        skip=True
    elif i==9 and skip:
        skip=False
    elif not skip :
        result+=i
print(result)
# print(sum(result))  # Output: 8
