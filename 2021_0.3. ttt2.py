import numpy as np

def determinwin(board):
    x1 = (board[0,0], board[0,1], board[0,2])
    x2 = (board[1,0], board[1,1], board[1,2])
    x3 = (board[2,0], board[2,1], board[2,2])
    y1 = (board[0,0], board[1,0], board[2,0])
    y2 = (board[0,1], board[1,1], board[2,1])
    y3 = (board[0,2], board[1,2], board[2,2])
    d1 = (board[0,0], board[1,1], board[2,2])
    d2 = (board[2,0], board[1,1], board[0,2])

    options = [x1, x2, x3, y1,y2,y3,d1,d2]
    for rowcol in options:
        if rowcol == (1,1,1):
            print("Player1 wins")
            return "w1"
        if rowcol==(2,2,2):
            print("player2 wins")
            return "w2"
    return False

def check_valid(board, row, col):
    v = True
    if (not (0 <= row < 3 and 0 <= col < 3) #guess in range
        or (board[row,col] != 0)): #guess spot already taken
        v = False
    return v

def getmove(current_player_sign, board, input_func=input, input_func2=input):
    # Get player1's moves, save as tuple, unpack tuple into two variables
    row,col = tuple(map(int,input_func("Player, make your move: ").split(",")))
    #check if move in range and available
    while check_valid(board, row, col) != True: 
        row,col = tuple(map(int,input_func2("Guess out of range or already in use, pick again: ").split(",")))
    #add move to board
    board_copy = board.copy()
    board_copy[row,col] = current_player_sign
    print(board_copy)
    return board_copy

def ttt(start_board=np.zeros((3,3,))):
    # Game intro
    print("Welcome to Tick Tack Toe. Enter your move as follows x,y")
    board = start_board
    win = False 
    count = 1
    while 0 in board and win == False:
        #to switch between players
        if count%2 != 0:
            curr_sign = 1
        else:
            curr_sign = 2
    #player one's move
        board = getmove(curr_sign, board_copy)
        win = determinwin(board)
        if win != False:
            return win 
        count += 1
    if 0 not in board and win == False:
        game_result = "Stale Mate"
        print(game_result) 
        return game_result
    return

# ttt()

#TEST

p1win = np.matrix([[1,1,1],[2,2,0],[2,0,0]])
p2win = np.matrix([[2,0,0],[0,2,0],[0,0,2]])
no_win = np.matrix([[0,1,1],[0,2,0],[0,0,2]])
stale_mate = np.matrix([[1,1,2],[1,1,2],[2,2,1]])
def test_determinwin():
    # pass in different boards
    assert determinwin(p1win) == "w1"
    assert determinwin(p2win) == "w2"
    assert determinwin(no_win) == False
    print("test_determinwin successful")
test_determinwin()

def top_left(prompt_message):
    return "0,0"
def out_of_range(promp_message):
    return "5,0"

def test_getmove():
    no1_win = no_win.copy() 
    no1_win[0,0] = 1
    no2_win = no_win.copy()
    no2_win[0,0] = 2
    assert np.array_equal(getmove(1, no_win, input_func=top_left), no1_win) 
    assert np.array_equal(getmove(2, no_win, input_func=top_left), no2_win) 
    assert np.array_equal(getmove(1, no_win, input_func=out_of_range, input_func2=top_left), no1_win) 
    print("test_getmove successful")
test_getmove() 

def test_check_valid():
    assert check_valid(no_win, 5, 1) == False #out of range
    assert check_valid(no_win, 2,2) == False #already taken
    assert check_valid(no_win, 0,0) == True  #valid move
    print("test_check_valid successful")
test_check_valid()

def test_ttt():
    assert ttt(start_board=stale_mate) == "Stale Mate"
    assert ttt(start_board=p1win) == "w1"
    assert ttt(start_board=p2win) =="w2"
    print("test_ttt successful")

print("ALL TESTS SUCCESSFUL")

    

