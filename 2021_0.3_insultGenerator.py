#project 3: insult generator
# ask the user facts about themself
#use these to generate personalized insults
import random

def info():
    name = input("What is your name? ")
    age = input("How old are you? ")
    sex = input("sex: male or female? ")
def insultgen:
    characteristic = [fat, stupid, ugly, uninspiring]
    person = [the Queen, Bugsbunny, Santa, hippo, ]
    randnum = random.randint(0,3)
    insult = name + " you're so " + characteristic[randnum] 
