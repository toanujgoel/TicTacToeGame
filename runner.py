# board
# display board
# select position to insert 0 or X
# Alternate turn
# Verify Winninf 
  # Horizontal
  # Vertical
  # Diagonal
# VErify Draw 

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_is_not_over = True
current_player = "X"
winner = None


def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "  ==>   1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "  ==>   4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "  ==>   7 | 8 | 9")
  print("\n")        

def check_if_game_over():
  global game_is_not_over

  row_winner = check_rows()
  column_winner=check_columns()
  diagonal_winner=check_diagonals()

  if row_winner or column_winner or diagonal_winner or "-" not in board:
    game_is_not_over=False

def check_rows():
  global winner
  if board[0]==board[1]==board[2] !='-':
    winner=board[0]
  elif board[3]==board[4]==board[5] !='-':
    winner=board[3]
  elif board[6]==board[7]==board[8] !='-':
    winner=board[6]  
  return True if winner else None

def check_columns():
  global winner
  if board[0]==board[3]==board[6] !='-':
    winner=board[0]
  elif board[1]==board[4]==board[7] !='-':
    winner=board[1]
  elif board[2]==board[5]==board[8] !='-':
    winner=board[2]
  return True if winner else None

def check_diagonals():
  global winner
  if board[0]==board[4]==board[8] !='-':
    winner=board[0]
  elif board[2]==board[4]==board[6] !='-':
    winner=board[2]
  return True if winner else None

def flip_player():
  global current_player
  if current_player == "X":
    current_player="0"
  elif current_player == "0":
    current_player="X"

def handle_turn(player):
    global game_is_not_over
    
    print(player+"'s turn")
    position = int(input("Input the position where you want to insert X or 0 : "))

    while (position not in [1,2,3,4,5,6,7,8,9]):
        position = input("Please Enter a valid position b/w 1 and 9 (including 1 and 9) : ")
    while(board[position-1] !="-"):
        position = input("You can't go there. It is already occupied by "+board[position-1]+". Please chose other available position : ")

    position = int(position)-1
    board[position] = current_player
    display_board()

def play_game():
  display_board()
  while (game_is_not_over):
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner == "X":
    print("X won.")
  elif winner == "0":
    print("0 won.")
  elif winner == None or "-" not in board:
    print("It's a tie")

play_game()
