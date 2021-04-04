#project 4: tic tac toe
#allow two players to play tic tac toe against each other
import numpy as np

def determinwin():
    x1 = board[0,0], board[0,1], board[0,2]
    x2 = board[1,0], board[1,1], board[1,2]
    x3 = board[2,0], board[2,1], board[2,2]
    y1 = board[0,0], board[1,0], board[2,0]
    y2 = board[0,1], board[1,1], board[2,1]
    y3 = board[0,2], board[1,2], board[2,2]
    d1 = board[0,0], board[1,1], board[2,2]
    d2 = board[2,0], board[1,1], board[0,2]

    # test_row = test_row

    options = [x1, x2, x3, y1,y2,y3,d1,d2]
    for rowcol in options:
        if rowcol.all() == 1:
            game_over = "Player1 wins"
            print(game_over)
            return game_over
        if rowcol.all()==2:
            game_over = "Player2 wins"
            print(game_over)
            return game_over
    return False

def getmove(player):
    # Get player1's moves, save as tuple, 
    pmove = tuple(map(int,input("Player, make your move: ").split(",")))
    #check if move in range and available
    if 0 > pmove[0] > 3 or 0 > pmove[1] > 3:
        pmove = tuple(map(int,input("Guess out of range, pick a move between (0,0) and (2,2)").split(",")))
    if pmove in p1 or pmove in p2:
        pmove = tuple(map(int,input("Position already taken, pick another move").split(",")))
    #save to list of all moves
    player.append(pmove)
    #add move to board
    board[player[-1]] = 1
    print(board)
    return board, p1

def ttt():
    # Game intro
    print("Welcome to Tick Tack Toe. Enter your move as a tuple (x,y)")
    board = np.zeros((3,3))
    #Reccord of players' moves
    p1 = []
    p2 = [] 
    win = determinwin()
    while 0 in board and win == False:
    #player one's move
        board, p1 = getmove(p1)
        win = determinwin()
        board,p2 = getmove(p2)
        win = determinwin() 
    if 0 not in board and win == False:
        return "Stale Mate"
    return determinwin()

ttt()
