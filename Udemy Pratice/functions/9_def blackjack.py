# def blackjack(a,b,c):
a,b,c=9,9,9
sum=a+b+c
if sum<=21:
    print(sum)
elif 11 in [a,b,c] and sum>21:
    print(sum-10)
else:
    print("BUST")