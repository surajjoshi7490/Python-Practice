
from random import shuffle
def dice_shuffel():
    dice_numbers=[1,2,3,4,5,6]
    student=None
    while True :
        shuffle(dice_numbers)
        student = int(input("Guess the number on the Dice : "))
        if dice_numbers[0]==student:
            break
        else :
              print(f"You have Gussed {student} But number is {dice_numbers[0]}")
    print(f"Awesome! You nailed it — that was the right guess! -:{student} ")


dice_shuffel()