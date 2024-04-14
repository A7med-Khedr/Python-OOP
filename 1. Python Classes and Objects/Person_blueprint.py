# Class Syntax
class Person: # First Class With Name Person
    """Person main class""" # Similar To Comment To Description Class
    def __init__(self, name, age, personID): # Constructor Function ( __init__ )
        # With Four Parameter And Self Is A Reference To Current Object
        self.name = name # To Set Name For Name Parameter
        self.age = age # To Set Age For Age Parameter
        self.personID = personID # To ID Name For ID Parameter

    def display_data(self): # Def Keyword To Declare A Function
        print("Hi my name is", self.name,",my age is", self.age, 
        "and my personID is", self.personID)

person01 = Person("Ahmed", 29, 120) # Object One
person02 = Person("Ronaldo", 35, 130) # Object Two
person03 = Person("Marcelo", 33, 125) # Object Three

print(person01.name) # Ahmed
print(person01.age) # 29
print(person01.personID) # 120

print(person02.name) # Ronaldo
print(person02.age) # 35
print(person02.personID) # 130

print(person03.name) # Marcelo
print(person03.age) # 33
print(person03.personID) # 125

person01.display_data() # To Display Full Data
person02.display_data() # To Display Full Data
person03.display_data() # To Display Full Data
