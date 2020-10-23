#Global variables

game_still_going = True

current_player  = "X"

winner = None

print("Tic Tac Toe")
#Board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

def print_board():
    print(board[0] + "|" + board[1] + "|" +board[2])
    print(board[3] + "|" + board[4] + "|" +board[5])
    print(board[6] + "|" + board[7] + "|" +board[8])

def check_if_win():
    global winner
    #check rows
    row_winner = check_rows()
    #check coloums
    coloums_winner = check_coloums()

    #check diagonlas
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif coloums_winner:
        winner = coloums_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
 
def check_rows():
   # Set global variables
   global game_still_going
   # Check if any of the rows have all the same value
   row_1 = board[0] == board[1] == board[2] != "-"
   row_2 = board[3] == board[4] == board[5] != "-"
   row_3 = board[6] == board[7] == board[8] != "-"
   # If any row have a match
   if row_1 or row_2 or row_3:
    game_still_going = False
   # Return the winner
   if row_1:
    return board[0] 
   elif row_2:
    return board[3] 
   elif row_3:
    return board[6] 
   else:
    return None

def check_coloums():
    #declaring global
    global game_still_going
    #check the columns of the board
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    #if any of them match
    if col_1 or col_2 or col_3:
        game_still_going = False
    #Return the winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

def check_diagonals():
    # Set global variables
  global game_still_going
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None

def check_if_tie():
    #Global variable
    global game_still_going 
    if "-" not in board:
        game_still_going = False
    return

def handle_turn(current_player):
    print(current_player + " 's turn.")
    position = input("Enter the position to mark on the board(from 1-9):")
    
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Invalid input choose position from 1-9:")

        position = int(position) - 1 

        if board[position] == "-":
            valid = True
        else:  
            print("You can't go there.")

    board[position] = current_player
    print_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def  flip_player():
    #Global variable
    global current_player
    #Switching current players for next turn 
    if current_player == "X":
       current_player = "O"
    elif current_player =="O":
       current_player = "X"
    return 

def play_game():

    #display initial board
    print_board()
    while game_still_going :
        
        #handle the turn a single player
        handle_turn(current_player)

        #check if game is over
        check_if_game_over()

        #flip to the other player
        flip_player()

    #Game ended
    if winner == "X" or winner == "O":
        print(winner + " Won.")
    elif winner == None:
        print("It is a Tie.")

#starting point of the game
play_game()

