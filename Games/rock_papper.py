from random import choice

Items = ['rock', 'paper', 'scissor']

def rock_paper():
    tie, lose, win = 0, 0, 0
    
    while True:
        # Taking input from user
        Your_item = input("Choose Rock, Paper, or Scissor (or type 'exit' to quit): ").lower()
        
        # if user wants to exit
        if Your_item == "exit":
            print(f"\nThanks for playing! Your final score is:")
            print(f"Tie: {tie}, Lose: {lose}, Win: {win}")
            break

        # if user enter invalid input
        if Your_item not in Items:
            print("Invalid input. Please choose from rock, paper, or scissor.")
            continue

        choice_value = choice(Items)

        if Your_item == choice_value:
            tie += 1
            print(f"Ooo it's a tie! You both chose {Your_item}.")
        elif (Your_item == "paper" and choice_value == "rock") or \
             (Your_item == "scissor" and choice_value == "paper") or \
             (Your_item == "rock" and choice_value == "scissor"):
            win += 1
            print(f"You won! {Your_item} beats {choice_value}.")
        else:
            lose += 1
            print(f"Oops, you lost! {choice_value} beats {Your_item}.")

        print(f"Current Score ➤ Tie: {tie}, Lose: {lose}, Win: {win}\n")

rock_paper()
