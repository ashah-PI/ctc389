# Arpita Shah
# CTC 389 -Lab# 8
#  function

again = "yes"

def choice1(input1):
    print("")
    print("You discover a dusty old map showing escape route. What do you want to do with map?")
    print("")
    print("1. Follow the marked trail")
    print("2. Ignore the map and explore freely")
    print("3. Tear the map open (something is inside)")
    option1 = int(input("Choose one of the following options."))
    if option1==1:
        print( name, " , as you are following the marked trail, you found the old bunker.")
        option10=choice2(option1)
        return option10
    elif option1==2:
        print( name, " , since you ignored the map;")
        option11=choice4(option1)
        return option11
    elif option1==3:
        print(name, ", you tear the map open and find a metal key which you used to call tribal warrior.")
        option12 = choice2(option1)
        return option12

    

def choice2(input2):
    print("")
    print("A tribal warrior appears and calls out to you.")
    print("")
    print("1. Ask the warrior for help")  
    print("2. Hide behind rocks")
    print("3. Offer the metal key you found")
    option3 = int(input("What do you choose? "))
    if option3==2:
        print(name,", as you were hiding behind the underground door.")
        option13= choice4(option3)
        return option13  
    if option3==1:
        print (name, ", a warrior appear infront of you and showed you the cave")
        option14= choice3(option3)
        return option14
    if option3==3:
        print(name, ", in exchange of the metal key you warrior showed you a way to the beach.")
        option15= choice3(option3)
        return option15

def choice3(input3):
    print("")
    print("You reach the base of the volcano. Smoke fills the air.")
    print("")
    print("1. Enter the lava tube tunnel")  
    print("2. Climb the outer ridge")
    print("3. Search for the old bunker")
    option4 = int(input("What do you choose? "))
    if option4==1:
        print(name, ", you have reached to the end of the tunel.")
        option16= choice4(option4)
        return option16
    if option4==2:
        print(name, ", you have found a key on the way..")
        option17= choice2(option4)
        return option17
    if option4==3:
        print(name, ", you found the old map in the old bunker.")
        option18=choice1(option4)
        return option18

def choice4(input4):
    print("")
    print("A loud alarm blares—the final evacuation is happening now!")
    print("")
    print("1. Board the rescue helicopter")  
    print("2. Sail away on a wooden raft")
    print("3. Ride a zipline across the canyon")
    option5 = int(input("What do you choose? "))
    if option5 == 1:
        print("The helicopter lifts off just as the volcano erupts." ,name , " , you have successfully escaped Volcano Island!")
    elif option5 == 2:
        print("The raft carries you away, but the waves grow violent.", name, ", you barely escape with your life!")
    elif option5 == 3:
        print("The zipline snaps halfway across the canyon.", name, ", you fall into the jungle and perish.")
    else:
        print(name, "your hesitation costs you precious time. The volcano erupts and you do not survive.")
    
    return option5



    #Main body
name = str(input("Welcome traveler!  What is your name? "))
while again =="yes" or again == "Yes" or again== "YES":
    
    print("Hello ", name , " you wake up on a mysterious island.  The ground shakes neneath you. A volcano at the center of the island is about to erupt.  You must escape")
    print(" ")
    print(" You see three possible paths in fornt of you. ")
    print ("************************************************************")
    print ("1. Cliimb the watch tower")
    print ("2. Go to the jungle")
    print ("3. Go to the beach")
    print ("************************************************************")
    option= int(input("what do you choose, before lava gets to you? "))
    
    if option==1:
        print( name, " , you just climbed the watch tower and reached the top.")
        option1=choice1(option)
    
    if option==2:
        print(name, " , you are in the jungle now. ")
        option2 = choice2(option)
    if option == 3:
        print (name, ", you are the beach where you can hear the sound of waves. Danger is still dangling.")
        opton3 = choice3(option)

    while option <1 or option>3 :
        option = int(input("Choose option from above. What do you choose? "))  

    print (" ")
    again = input("Would you like to play again? (yes/no)")
print("Thank you for playing! Have a mathemagical day!")

