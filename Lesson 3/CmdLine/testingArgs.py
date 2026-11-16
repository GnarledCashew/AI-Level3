class cars(): # Defines the class cars
    
    #Attributes given to the class that define how the class works
    doors = [4,2,1]
    wheels = [4,3,0]
    engine = True
    breaks = True


carB = cars() # Defines the object 'carB'
carB.wheels = cars.wheels[0] # changes the attribute of the object from the class

carA = cars() # Degfines the object 'carA'


#Prints the number of wheels the car has
print(f"Car A has thit many wheels: {carA.wheels}.")
print(f"Car B has thit many wheels: {carB.wheels}.")

