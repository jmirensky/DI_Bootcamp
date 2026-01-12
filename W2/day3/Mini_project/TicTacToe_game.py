#Mini-Project - Tic Tac Toe

print("\nWelcome to TIC TAC TOE\n")

#Step 1: Representing the Game Board
#board  is a list of 3 lists with 3 empty positions each = 9 empty cells (represented with blank spaces)

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

#Step 2: Displaying the Game Board = with nice format
def display_board(board): 
    print(f'* {board[0][0]} | {board[0][1]} | {board[0][2]} *' )
    print("-" * 13)
    print(f'* {board[1][0]} | {board[1][1]} | {board[1][2]} *' )
    print("-" * 13)
    print(f'* {board[2][0]} | {board[1][2]} | {board[2][2]} * \n')


#Step 3: Getting Player Input
def player_input(player, board):
    while True:            #keeps the loop going until the player enters something valid.
        try:
            row = int(input(f'Player {player}, choose the row (0, 1, 2): '))  
            col = int(input(f'Player {player}, choose the column (0, 1, 2): '))  
  
            # Verify row/column within the range
            if row not in range(3) or col not in range(3):
                print("Invalid position. Row and column must be 0, 1, or 2.")
                continue   #comeback to input
            
            # Verify thaty cell is empty
            if board[row][col] != ' ':
                print("That cell is already occupied. Try again.")
                continue    #return to input
            
            return row, col  # Returns valid position
        except ValueError:
            print("Please enter valid integers for row and column.")  #to allow just numbers


#Step 4: Checking for a Winner
def check_win(board, player):

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True    # there is a winner if all cells in the row belong to the current player

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True     #There is a winner if, when traversing each column, the elements are the same for any column.

    # Check main diagonal   (0,0), (1,1), (2,2)
    if all(board[i][i] == player for i in range(3)):
        return True    # there is a winner

    # Check secondary diagonal   (0,2), (1,1), (2,0)
    if all(board[i][2-i] == player for i in range(3)):
        return True   # there is a winner

    return False  # There is no winner


#Step 5: Checking for a Tie
def check_tie(board):
    for row in board:         #Explore each row of the board
        if ' ' in row:        #If it finds one empty space... 
            return False      #the game can still continue --> there's no tie
    return True               #the board is full -->  it's a tie


#Step 6: The Main Game Loop   --> The heart of the game is play function

def play():
    # 1. Initialize board
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    # 2. Starting player
    current_player = 'X'

    # 3. Main loop of the game
    while True:
        display_board(board)

        # 4. Get player movement
        row, col = player_input(current_player, board)
        board[row][col] = current_player

        # 5. Check if there s a winner
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        # 6. Check tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # 7. Change player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


play()