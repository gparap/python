#
# A simple number guessing game prototype
# Created by gparap
#
import random
guesses = 5
print ("****************************************")
print ("We are playing 'Guess the number' [1-10]")
print ("You have 5 guesses")
while 1:
    print ("****************************************")
    #check if it's a valid input
    try:
        input_n1 = int((input("Your guess: ")))
    except ValueError:
        print ("This is not a number, smarty!")
        continue

    guesses -= 1

    #randomize
    random_n2 = random.randrange(1,10)
    print ("My number was: " ,random_n2)

    #info the player
    if guesses != 0:
        print ("Your guesses left: " + str(guesses))
    
    #end the game
    if input_n1 == random_n2:
        print("SUCCESS!\n")
        print("Your success ratio is: " + str(int(100/guesses)) + "%")
        break
    elif guesses == 0:
        print("Sorry, you lose..")
        break