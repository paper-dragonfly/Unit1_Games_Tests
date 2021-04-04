#Level 0.2 Rock Paper Scissors

import random

# def RPS():
#     print("Welcome to rock, paper, scissors. Choose your weapon. Type \"exit\" to end game")
#     player = None
#     choices = ["rock", "paper", "scissors"]
#     while player != "exit":
#         player = input("rock,paper, scissors?: ")
#         comp = choices[random.randint(0,2)]
#         print("Computer guessed: " + comp)
#         if (player == "rock" and comp == "scissors") or (player == "paper" and comp == "rock") or (player == "scissors" and comp == "paper"):
#             print("Computer choice: "+comp+ " | You win")
#         if (player == "rock" and comp == "paper") or (player == "paper" and comp == "scissors") or (player == "scissors" and comp == "rock"):
#             print("You Lose")
#         if (player == "rock" and comp == "rock") or (player == "paper" and comp == "paper") or (player == "scissors" and comp == "scissors"):
#             print("Computer choice: "+comp+ " | DRAW")        
#     print("Thanks for playing")
#     return 

def comp_choice():
    choices = ["rock", "paper", "scissors"]
    conv = {"rock":1, "paper":2, "scissors":3}
    return choices[random.randint(0,2)]


def RPS2(player_input = None, input_func_player=input, input_func_comp=comp_choice):
    print("Welcome to rock, paper, scissors. Choose your weapon. Type \"exit\" to end game")
    player = player_input
    choices = ["rock", "paper", "scissors"]
    conv = {"rock":1, "paper":2, "scissors":3}
    result = {
        (1,2):"L", 
        (1,3):"W", 
        (2,1): "W", 
        (2,3): "L", 
        (3,1):"L", 
        (3,2):'W'
    }
    while player != "exit":
        player = input_func_player("rock,paper, scissors?: ")
        comp = input_func_comp 
        print("Computer guessed: " + comp)
        if player == comp:
            outcome = "draw"
            print(outcome)
            return outcome
        else:
            tup = (conv[player],conv[comp])
            outcome = (result[tup]) 
            print(outcome)
            return outcome

    game_over = "Thanks for playing" 
    print(game_over)
    return game_over

# RPS2()

#TEST 
def rock(prompt_message):
    return "rock" 

def test_RPS():
    #check "exit" --> "thanks for playing"
    assert RPS2(player_input="exit") == "Thanks for playing"
    #check draw case
    assert RPS2(player_input=None, input_func_player=rock, input_func_comp="rock") == "draw"
    assert RPS2(player_input=None, input_func_player=rock, input_func_comp="paper") == "L"
    assert RPS2(player_input=None, input_func_player=rock, input_func_comp="scissors") == "W"
    print("test successful")

test_RPS()