#CODE
def RPS2():
    print("Welcome to rock, paper, scissors. Choose your weapon. Type \"exit\" to end game")
    player = None
    choices = ["rock", "paper", "scissors"]
    conv = {"rock" : 1, "paper":2, "scissors":3}
    result = {
        (1,2):"L", 
        (1,3):"W", 
        (2,1): "W", 
        (2,3): "L", 
        (3,1):"L", 
        (3,2):'W'
    }
    while player != "exit":
        player = input("rock,paper, scissors?: ")
        while player != "rock" and player != "paper" and player != "scissors":
            player = input("you did not select a valid choice, try again: ")
        comp = choices[random.randint(0,2)]
        print("Computer guessed: " + comp)
        if player == comp:
            print("Draw")
        else:
            tup = (conv[player],conv[comp])
            print(result[tup])         
    return print("Thanks for playing")

#TEST
#1. does typing "exit" end the game
#2. 