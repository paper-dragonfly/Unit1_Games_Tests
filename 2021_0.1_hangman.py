# Level 0.1 Hangman
# project 1: make a hangman game
#   player one seeds the game with a word
#   player two guesses, one letter at a time
#   after each guess, the word with the spaces and filled in letters appears
#   there should also be a hangman counter: after N misses, the player loses

# def hangman():
#     wordp1 = input("Player 1, input a word: ")
#     wordp1 = wordp1.lower()
#     wordp2 = "_ "*len(wordp1)
#     print(wordp2)
#     hang_count = 9
#     while hang_count > 0: 
#         if not "_" in wordp2:
#             print("Congratulations you got it! The word is " + wordp2)
#             return
#         guess = input("Player 2, guess a letter ")
#         guess = guess.lower()
#         if guess in wordp1:
#             letter_position = [pos for pos, let in enumerate(wordp1) if let == guess]
#             letter_position = list(map(lambda x:x*2, letter_position))
#             for pos in letter_position:
#                 wordp2 = wordp2[0:pos] + guess + wordp2[pos+1:]            
#             print(wordp2)
#         else:
#             hang_count += -1
#             print("Nope! You have " + str(hang_count) + " guesses remaining" )
#     print("Sorry you lost, the word was: " + wordp1)
#     return

#hangman()

def show_prog(guesses, correct_word):
    guess_prog = [char if char in guesses else "_" for char in correct_word]
    print(" ".join(guess_prog))
    return guess_prog

def hangman2():
    wordp1 = input("Player 1, input a word: ")
    wordp1 = wordp1.lower()
    wlist = list(wordp1)
    glist = []
    hang_count = 9
    while hang_count > 0: 
        guess_prog = show_prog(glist, wlist)
        if "_" not in guess_prog:
            print("Congratulations you got it! The word is " + wordp1)
            return
        guess = input("Player 2, guess a letter ")
        guess = guess.lower()
        glist.append(guess)
        if guess not in wlist:
            hang_count += -1
            print("Nope! You have " + str(hang_count) + " guesses remaining" )
    print("Sorry you lost, the word was: " + wordp1)
    return


hangman2()



