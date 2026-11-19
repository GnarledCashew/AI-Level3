import random  # imports the random library

# uses while loop and decision making
# guess the number program

def welcome(): # Starts the game and stores the users game range
    print("Welcome to the guessing game, how would you like to play today?")
    gamemode = str(
        input("""
A) Range 1-100
B) Range 1-50
C) Range 1-25
  """)
    )
    gamemode = gamemode.lower() # Uses the built in function 
                                # to force the answer into lowecase
    return gamemode


def modeSelector(usrInput): # Defines how large the random number could be 
    if(usrInput in ["a", "b", "c"]):
      if(usrInput == "a"):
        print("Your range is 1-100 \n") # shows user and looks nicer on the output
        randGoal = random.randint(1, 100) # Uses .randint to create a random 
      elif(usrInput == "b"):              # integer between the range. 
        print("Your range is 1-50 \n")
        randGoal = random.randint(1, 50)
      elif(usrInput == "c"):
        print("Your range is 1-25 \n")
        randGoal = random.randint(1, 25)
      return randGoal # allows the data to be stored to a variable
    else:
      print("Not a valid input!") # error handling
    

#Main program

playerChoice = welcome() # Calls function and stores to variable

# variable is parsed into function, outputting the games goal number
guessNum = modeSelector(playerChoice)
# stores the players initial guess
plyrGuess = int(input("What's your first guess?")) 

 # starts a loop that breaks when the guessNum is guessed
while (plyrGuess != guessNum):

  # a variable used to change dialogue
  howclose = int(guessNum - plyrGuess) 
  
  if (plyrGuess > guessNum): # checks if guess is higher 
    #embedded if statement
    if(howclose in range (-6, 1)): # checks range of 'howclose' different text depending on result 
      print("You're so close, just a little lower!! \n")
    else:
      print("You're too high! \n")
  elif (plyrGuess < guessNum): # checks if guess is lower
    if(howclose in range (0, 6)):
      print("You're so close, just a little higher!! \n")
    else:
      print("You're too low! \n")


  plyrGuess = int(input("What's your next guess? \n")) # takes the players next guess and loops

print("Well done you got it!") # winning message.
  