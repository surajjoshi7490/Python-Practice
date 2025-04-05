from random import choice
Items=['rock','papper','scissor']
tie , loose , win=0
def rock_papper():
    Your_item=None
    do 
    while True:
        choice_value=choice(Items)
        Your_item=input("Rock \nPapper \nScissor \nWhat is your Item Among these :-  ").lower()
        if Your_item==choice_value:
            print(f"Ooo It's a Tie {Your_item} and {choice_value} ")
            tie +=tie
        elif ( Your_item== "papper" and  choice_value== "rock" ) or \
             ( Your_item=="scissor" and choice_value=="papper") or\
             ( Your_item=="rock" and choice_value=="scissor"):
            print(f"you have won {Your_item} and {choice_value} ")
            win +=win
        else:
            print(f"Opps you loose {Your_item} and {choice_value}")
            loose += loose
        print(f"This is your score Tie:{tie}\nLoose {loose}\nwin {win} ")

           
    
    #     else:
    #         print(f"Opps Your Guess is {Your_item} and My Guess is {choice_value} ")
    # print(f"Amazing You got the right Guess {Your_item}  , {choice_value}")

rock_papper()