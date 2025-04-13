def display_rows(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

def tic_toc():
    choice='wrong'
    while choice not in ['X','x','O','o']:
        choice=input("Which One whould you chose : Xs or Os ")
        if choice not in ['X','x','O','o']:
            print("Please select the valid one ")
    return choice.upper()
def in_which_row():
    position='wrong'
    while position not in ['R11','R12','R13','R21','R22','R23','R31','R32','R33']:
        position=str(input("From which Row you would like to place your frist :\n R11-R2-R3\nR21-R22-R23\nR31-R32-R33"))
        if position not in ['R11','R12','R13','R21','R22','R23','R31','R32','R33']:
            print("You ahve not given a valid input")
    return position
def update_board(position, mark, row1, row2, row3):
    mapping = {
        'R11': (row1, 0), 'R12': (row1, 1), 'R13': (row1, 2),
        'R21': (row2, 0), 'R22': (row2, 1), 'R23': (row2, 2),
        'R31': (row3, 0), 'R32': (row3, 1), 'R33': (row3, 2)
    }

    row, index = mapping[position]
    if row[index] == '':
        row[index] = mark
        return True
    else:
        print("Position already taken! Try again.")
        return False
def check_winner(row1,row2,row3,mark):
    # Row
    if row1.count(mark)==3 or row2.count(mark)==3 or row3.count(mark)==3:
        return True
    # coloumn
    for i in range(3):
        if row1[i]==mark and row2[i]==mark and row3[i]==mark:
            return True 
    # Diagonal 
    if row1[0]==mark and row1[1]==mark and row3[2]==mark:
        return True
    if row1[2]==mark and row2[1]==mark and row3[0]==mark:
        return True 
    return False 

# number=int(input(f"In {row} where would you like to place :\n 1 \n 2 \n 3"))
row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']

current_mark =tic_toc()
game_on = True

while game_on:
    display_rows(row1, row2, row3)

    print(f"\n🕹️  It's {current_mark}'s turn!")  # 🆕 New line added

    pos = in_which_row()
    
    success = update_board(pos, current_mark, row1, row2, row3)
    if not success:
        continue  # ask again if spot already taken

    if check_winner(row1, row2, row3, current_mark):
        display_rows(row1, row2, row3)
        print(f"\n🎉 Player {current_mark} wins!")
        break

    # Alternate player
    current_mark = 'O' if current_mark == 'X' else 'X'

    # Check for draw
    if all(cell != '' for cell in row1 + row2 + row3):
        display_rows(row1, row2, row3)
        print("\n🤝 It's a draw!")
        break
