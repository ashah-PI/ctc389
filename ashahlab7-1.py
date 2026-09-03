# Arpita Shah
#Lab 7
#CTC 389

guess=int(input("Guess my number:  "))

while ((abs(67-guess))<=2 and (abs(67-guess)>0)):
    guess= int (input(" You are close, but not exact. Try again "))
if (guess == 67):
    print("You did it!  You guess my number. ")
else:
    print ("Sorry, you lost.  Your guess was higher than my number which is 67")
