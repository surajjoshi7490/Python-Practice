
def display_list(game_list):
    print("Here is your  Game List")
    print(game_list)

def position_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice=input("Where Do you wants to change the value")
        if choice not in ['0','1','2']:
            print("you have entered wrong input")
    return int(choice)
def replacement_choice(game_list,position):
    
    user_placement=input("Type a string to place at the positon ")
    game_list[position]=user_placement
    return game_list
def want_play_again():
    want='wrong'
    while want not in ['y','Y','N','n']:
        want=input("Do You want to play more : Y / N ")
        if want not in ['y','Y','N','n']:
            print("You Have given wrong input")
        
    return want

mylist=[0,1,2]
display_list(mylist)
position = position_choice()
print(replacement_choice(mylist,position))



