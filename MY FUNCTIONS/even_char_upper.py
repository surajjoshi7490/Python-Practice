def new(stri):
    for i in range(len(stri)):
        if i%2==0 :
            print(stri[i].upper(),end='')
        else :
            print(stri[i],end='')