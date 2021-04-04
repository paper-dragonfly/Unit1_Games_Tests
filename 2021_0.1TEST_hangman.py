#How to write a test - Nico's example
def turntoint(val):
    return int(val)

def test_turntoint():
    # test that it works with proper value
    assert turntoint(1.2) == 1
    # test that it fails if bad input
    try:
        turntoint("wqeqwe")
        print('It didnt break but should')
    except:
        print('It broke as expected!')

# test_turntoint()

 ##########################################
 #HANGMAN GAME
def eval_prog(guesses, correct_word):
    guess_prog = [char if char in guesses else "_" for char in correct_word]
    return guess_prog

def check_win(guess, correct_word, wlist, glist, hang_count):
    terminate = False
    new_glist = glist + [guess]
    guess_prog = eval_prog(new_glist, wlist)
    print(' '.join(guess_prog))
    
    if "_" not in guess_prog:
        print("Congratulations you got it! The word is " + correct_word) 
        terminate = True
    elif guess not in wlist:
        hang_count += -1
        print("Nope! You have " + str(hang_count) + " guesses remaining" )
    return (new_glist, hang_count, terminate)

def hangman2(wordp1, hang_count, glist=[], input_func=input):
    wordp1 = wordp1.lower()
    wlist = list(wordp1)
    hang_count = hang_count
    guess_prog = ["_" for char in wordp1]
    print(" ".join(guess_prog))
    while hang_count > 0: 
        player_input = input_func("Player 2, guess a letter ").lower()
        if len(player_input)!= 1:
            player_input = input_func("Input must be a single letter ").lower()
        glist, hang_count, terminate = check_win(player_input,wordp1, wlist, glist, hang_count)
        if terminate == True:
            return True
    print("Sorry you lost, the word was: " + wordp1)
    return False 

hangman2("tip",8)

#TEST:
#1. Given a correct input and correct guesses --> "Congrats..."
#2. Given correct input and incorrect guess -- > "Nope!..."
#3. Given correct input and incorrect guesses --> "Sorry..."
#4. words = cat, ticket, town guesses = [c,a,t, i, c, k, e, f, s, h]
def test_eval_prog():
    input_word = list("ticket")
    guess1 = list("tick")
    guess2 = list("house")
    guess4 = [1,2,4]
    assert eval_prog(guess1, input_word) == ['t', 'i', 'c', 'k', '_', 't']
    assert eval_prog(guess2, input_word) == ['_', '_', '_', '_', 'e', '_']
    assert eval_prog(guess4, input_word) == ['_', '_', '_', '_', '_', '_']
    print("test_eval_prog successful")
    
# test_show_prog()

#test_check_win
#1. gletter -> win: print "congrats...", return new_glist = wlist(no duplicates), hang_count, terminate = True
#2. gletter correct but no win yet -> return new_glist, hang_count, terminate = False
#3. gletter not in wlist: print "nope...", return new_glist = glist + gletter, hang_count -1, terminate = False 
def test_check_win():
    input_word = "ticket to ride"
    wlist = list(input_word)
    hang_count = 8
    winning_glist = list("ticke ord")
    nearwin_glist = list("ticke or")
    twooff_glist = list("ticke o")
    gletter_win = "d"
    gletter2 = "f"

    assert check_win(gletter_win, input_word, wlist, nearwin_glist, hang_count) == (list("ticke ord"), 8, True)
    assert check_win(gletter_win, input_word, wlist, twooff_glist, hang_count) == (list("ticke od"), 8, False)
    assert check_win(gletter2, input_word, wlist, twooff_glist, hang_count) == (list("ticke of"), 7, False)
    print("test_check_win successful")
#thought: using sets would be better than using lists for many of these
#sets: order doesn't matter and objects are unique 

# test_check_win() 

#Hangman Test
#1. player inputs a winning letter
#2. Player looses (hang_count = zero) ->
def letter_e(prompt_message):
    return "e"
def letter_f(prompt_message):
    return "f" 

def test_hangman2():
    ##Testing when player wins
    assert hangman2("ticket", 5, glist = list("tickqx"), input_func=letter_e) == True
    # assert hangman2("ticket", 5, glist=list("tic"), input_func = letter_e) == False
    ## Testing when hang_count runs out
    assert hangman2("ticket", 0, glist=list("tic"), input_func = letter_e) == False
    ##Testing when user inputs an incorrect letter
    assert hangman2("ticket", 2, glist=list("tic"), input_func = letter_f) == False
    print("test_hangman2 succeful")

# test_hangman2()

