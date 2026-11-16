from ascii import asciiart
def welcome(): # Defines the function for welcoming the user
  print("Welcome, how are you doing today on a scale of 1-3?")
  usrFeels=int(input()) # Takes data from user input
  return usrFeels #returns the data so that it can be stored to a variable.

def asciiFeels(EmScore): # Function that takes a perameter, the users input from def welcome()
  if(EmScore == 1): # An if statement that starts an elif chain
    print("sorry to hear that, hope you feel better soon!")
    asciiart.outputheart() 
  elif(EmScore == 2):
    print("You got this, only ups from here!")
    asciiart.outputthumb()
  elif(EmScore == 3):
    print("On top of the world eh?")
    asciiart.outputearth() # calls the class then the function.
  else:
    print("Not a valid input!") # ends the chain & error handles a non valid input.
    asciiart.outputSad()
# ----------------
# Main program
# ----------------
number = welcome() # calls the welcome function and stores the value in the variable number.

asciiFeels(number) # calls the function using 'number' as a parameter.

#CHALLENGE, create a new subprogram which displays a welcome message to the user
#CHALLENGE, create a new subprogram which should display another piece of ASCII art 
#use https://www.asciiart.eu/ to find some ASCII art