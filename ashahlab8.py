# Arpita Shah
# CTC 389 - Lab 8

again ="yes"

def choice1(input1):
    print("")
    print("You discover a dusty old map showing escape route. What do you want to do with map?")
    print("")
    print("1. Follow the marked trail")
    print("2. Ignore the map and explore freely")
    print("3. Tear the map open (something is inside)")
    option2 = int(input("What do you choose? "))
    while option2 <1 or option2>3 :
        option2 = int(input("Choose option from above. What do you choose? "))  
    return option2

def choice2(input2):
  print("")
  print("A tribal warrior appears and calls out to you.")
  print("")
  print("1. Ask the warrior for help")  
  print("2. Hide behind rocks")
  print("3. Offer the metal key you found")
  option3 = int(input("What do you choose? "))
  while option3 <1 or option3>3 :
    option3 = int(input("Choose option from above. What do you choose? "))  
  return option3

def choice3(input3):
    print("")
    print("You reach the base of the volcano. Smoke fills the air.")
    print("")
    print("1. Enter the lava tube tunnel")  
    print("2. Climb the outer ridge")
    print("3. Search for the old bunker")
    option4 = int(input("What do you choose? "))
    while option4 <1 or option4>3 :
        option4 = int(input("Choose option from above. What do you choose? "))  
    return option4

def choice4(input4):
    print("")
    print("A loud alarm blares—the final evacuation is happening now!")
    print("")
    print("1. Board the rescue helicopter")  
    print("2. Sail away on a wooden raft")
    print("3. Ride a zipline across the canyon")
    option5 = int(input("What do you choose? "))
    while option5 <1 or option5>3 :
        option5 = int(input("Choose option from above. What do you choose? "))  
    return option5

while again =="yes" or again == "Yes" or again== "YES":
    name = str(input("Welcome traveler!  What is your name? "))
    print("Hello ", name , " you wake up on a mysterious island.  The ground shakes beneath you. A volcano at the center of the island is about to erupt.  You must escape")
    print(" ")
    print(" You see three possible paths in front of you. ")
    print ("************************************************************")
    print ("1. Climb the watch tower")
    print ("2. Go to the jungle")
    print ("3. Go to the beach")
    print ("************************************************************")
    option= int(input("what do you choose, before lava gets to you? "))
    while option <1 or option>3 :
        option = int(input("Choose option from above. What do you choose? "))  

    option2=choice1(option)
    option3 =choice2(option2)
    option4 = choice3(option3)
    option5 = choice4(option4)

    if option5 == 1:
        print("The helicopter lifts off just as the volcano erupts." ,name , " you have successfully escaped Volcano Island!")
    elif option5 == 2:
        print("The raft carries you away, but the waves grow violent.", name, "you barely escape with your life!")
    elif option5 == 3:
        print("The zipline snaps halfway across the canyon.", name, "you fall into the jungle and perish.")
    else:
        print(name, "your hesitation costs you precious time. The volcano erupts and you do not survive.")

    print (" ")
    again = input("Would you like to play again? (yes/no)")
print("Thank you for playing! Have a mathemagical day!")
