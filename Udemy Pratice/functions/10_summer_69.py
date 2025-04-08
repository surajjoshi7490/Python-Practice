def summer_69(arr):
    value=0
    skip=False
    for i in arr:
        if i==6:
            skip=True
        elif i==9  and skip:
            skip=False
        elif not skip:
            value+=i
    return value
        

print(summer_69([4, 5, 6, 7, 8, 9]))