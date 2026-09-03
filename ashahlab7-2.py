# Arpita Shah
#Lab 7
x=2
def guesnum(guess):
    while (guess==65 or guess==66 or guess==68 or guess==69):
        guess= int (input(" You are close, but not exact. Try again "))
    if (guess == 67):
        print("You did it!  You guess my number. ")
    else:
        print ("Sorry, you lost.  Your guess was higher than my number which is 67")


while (x>1):
    ask = str(input("Would you like to play the game, yes or no?  "))
    if (ask=="yes"):
        number=int(input("Guess my number:  "))
        guesnum(number)
    else:
     x= 0
     print(":-( ")
