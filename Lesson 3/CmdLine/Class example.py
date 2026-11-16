class cars(): # Defines the class cars
    
    #shows how each instance of the class should be defined 
    def __init__(self, wheels, doors, colour):
        #Attributes given to the class that define how the class works
        self.wheels = wheels
        self.doors = doors
        self.colour = colour
    engine = "V-6"
    windows = [4,2,8]
    brakes = True
    
    # defines a function the extrapolates the data from the object and uses it in the string
    def coolCar(self):
        print(f"Nice car, {self.colour} is my favourite!.")
 
carA = cars(12, 64, "Blue") # Degfines the object 'carA' using data given

#Prints the details of the car
print(f"""Details of your car: 
wheels: {carA.wheels}
doors: {carA.doors}
colour = {carA.colour}
engine = {carA.engine}
windows = {carA.windows[0]} # picks the item from the list defined
brakes = {carA.brakes}
      """)

# calls the function on the object 'carA'
carA.coolCar()

