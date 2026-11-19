# PERSONAL STATEMENT GENERATOR.
# This program will demonstrate how we can create variables, use data types and obtain inputs
#declare variables and assign values
print("This programe will help you write your personal statement for your CV by taking in some general information \n")

#CHALLENGE can you add more questions?
# Questions to ask user
fullname=input("What is your name? ") # string
age=int(input("How old are you? ")) #take an input from the user to make our programs interactive 
height=float(input("How tall are you?")) # float
cmorinch=input("CM or Inch?" ) 
homeowner=bool(input("I own a house, True or False? ")) # Boolean
pet=input("Do you own a pet? ") # String
interests=input("What do you do for fun? ") # String

#Changes the boolean answer into a string
if(homeowner == False or "No" or "no"):
  houseStatus = " and I don't own a house."
else:
  houseStatus = " and I own a house."

print("\n") #seperates the text in output
print("My name is " + fullname + ". I am " + str(age) + 
      " and sit at " + str(height)) + cmorinch + " I own "+ pet+" and I like the " + interests + houseStatus 
#CHALLENGE output the rest of the data in this format


