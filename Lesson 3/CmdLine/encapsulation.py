#defines the class cars
class cars():
    
    # creates a list to add the user dat to.
    carlist = []
    
    #initialises how the data should be input into the class
    def __init__(self, ownerName, carModel):
        self.__ownerName = ownerName #private variable
        self.carModel = carModel #regular variable
        cars.carlist.append(self)
    
    #determins how data enterd should be displyed when called as a list
    def __repr__(self):
        return f"Car(Owner: {self.__ownerName}, Model: {self.carModel})"
    
    #only way to print a private variable
    def display():
        print(f"This is the list {cars.carlist}")     

#creates a new object to add to the list
carA = cars("Rhys", "N/A")
carB = cars("Jeff", "Mazda")
carC = cars("Dave", "BMW")

#usues function to display the list
cars.display()

#throws an error as '__ownerName' cannot be accessed outside of the class.
print(carA.__ownerName)
