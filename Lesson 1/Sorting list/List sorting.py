print("Going shopping? Don't forget your list! \n")

#Defines the list's peramaters
class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    # This helps print the object nicely
    def __repr__(self):
        return repr((self.name, self.quantity))

# The list provided to the user at the start
shoppinglistA = [
    Item('Banana', 6), # Each item is provided with a name and a quantity
    Item('Apples', 12),
    Item('Biscuits', 2),
    Item('Tomatoes', 3),
    Item('Yogurt', 4),
]
print(shoppinglistA) # Prints the list to the user
print("\n") # Creates space on the output screen

#Allows the user to add to the list
forget=input("Did you forget anything? Yes or No \n") 

while(forget.lower() == "yes"): #Loops until the user says no, allowing the addition of infinite items
  item=input("What did you forget? \n") #The first perameter of the list item
  amount=int(input("How many do you need? \n")) #Second perameter of the list item
  shoppinglistA.append(Item(item, amount)) # Adds the item & quantity to the list
  print(shoppinglistA) # Returns the new list
  forget=input("Anything else to add? \n") # continues or breaks the loop
  if(forget.lower() != "yes"):
    break

# sorts the list to the users perogative.
order=input("""How would you like it sorted?
A) Alphabetically
B) Numerically
C) Both \n""")

if(order.lower()=="a"): # Alphabetical sort
  shoppinglistA.sort(key=lambda Item: Item.name)
  print("Alphabetical:", shoppinglistA)
elif(order.lower()=="b"): # Numerical sort
  shoppinglistA.sort(key=lambda Item: Item.quantity)
  print("Numerical:", shoppinglistA)
elif(order.lower()=="c"): # Both sorts together
  shoppinglistA.sort(key=lambda Item: Item.quantity)
  print("Numerical:", shoppinglistA)
    shoppinglistA.sort(key=lambda Item: Item.name)
  print("Alphabetical:", shoppinglistA)
else: # Error handling
  print("Don't wanna go shopping eh?")