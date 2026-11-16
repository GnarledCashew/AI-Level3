def attempts(tries): # defines the code for counting the players number of input attempts

  # because computer counting starts at 0, the + 1 is there to make it readable to prople
  print("Your on try no. " + str(tries + 1)) 
  tries += 1 # adds to trirs and stores it again.
  return tries #  returns the new value of tries 

#MAIN PROGRAM

#password username checker program
# Defines all variables
tries = 0 # number of player attempts
corName = False #  boolean to end while loop
corPass = False # boolean to end while loop
actualpassword="password" #assignment operator
actualusername="rhyshud" #assignment operator

# While loop checks to see if the user inputs the password correctly 
#Ends when tries reaches 5 or the right password is entered
while (tries != 6 and corPass == False): 
    passwordentered = str(input("Enter your password \n")) #assignment operator
    if (passwordentered!=actualpassword): #relational operator 'not equal to'
      print("Invalid password \n")
      tries = attempts(tries) # calls attempts function and updates the tries variable when called
      if (tries == 5): # ends the program when called
        print("You ran out of tries please wait \n")
        break
      
    else:  # program continues onto the next loop
      print("Valid password")
      corPass = True
    

# While loop checks to see if the user inputs the username correctly 
#Ends when tries reaches 5 or the right username is entered
while (tries != 5 and corName == False):
  usernameentered=str(input("Enter your username \n")) #assignment operator
  if (passwordentered!=actualpassword) or (usernameentered!=actualusername): #logical operator 'or'
      print("Invalid username \n")
      tries = attempts(tries)# calls attempts function and updates the tries variable when called
      if (tries == 6):
        print("You ran out of tries please wait \n")
        break
  else:  
      print("Valid username \n")
      corName = True
      print("You have logged in successfully thank you \n") # ends the program with a message if all information is correct.
      