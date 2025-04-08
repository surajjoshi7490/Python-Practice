def find_33():
    has_33=[1,2,3,3]
    for i in range(len(has_33)-1):
     if has_33[i]==3 and has_33[i+1]==3:      
        return True
    return False
print(find_33())

    
    