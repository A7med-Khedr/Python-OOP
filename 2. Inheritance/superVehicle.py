# Inheritance
# Parent class
class Vehicle: # Class Keyword To Define Class With Name Vehicle
    def Vehicle_data(self): # def To Define A Function And Self Parameter
        print("Hello from the Vehicle class!")

# Car Child class
class Car(Vehicle): # Another Class To Inherit All Attribute And Method In Vehicle
    def Car_data(self):  # Function In Car Class With Function In Vehicle
        print("Hello from the Car class!")

# Bike Child class
class Bike(Vehicle): # Another Class To Inherit All Attribute And Method In Vehicle
    def Bike_data(self):  # Function In Bike Class With Function In Vehicle
        print("Hello from bike!")

# Objects based on Car
car01 = Car() # Object One To Car Class
bike01 = Bike() # Object One To Bike Class

# Get Vehicle data
car01.Vehicle_data() # Access In A Function In Vehicle Class With Inherit
car01.Car_data() # Function In Car Class
print("=============")
bike01.Vehicle_data() # Access In A Function In Vehicle Class With Inherit
bike01.Bike_data() # Function In Bike Class
