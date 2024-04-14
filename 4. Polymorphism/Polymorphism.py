# Polymorphism It Is Use The Same Method To Different Tasks
# Using Polymorphic built-in functions
print(len("Anaconda"))  # 8 Characters
print(len([5, 15, 20, 25])) # 4 elements
# Use Len Method To Different Task

#  Using Polymorphic User-defined functions
def add(x, y, z = 0):
    return x + y + z
print(add(5, 7)) # 12
print(add(5, 7, 9)) # 21

# Method Overriding
class Bird:
    def intro(self): # Method To Get Task With The Same Result In All Instance
        print("Hi, there are many types of birds!")
    
    def flight(self): # Flight Method It Is A Function With A Different result In Bird
        print("Most of birds can fly but some cannot!")
# Sparrow child class
class Sparrow(Bird): # Child Class From Bird With Inherit All Method And Attribute
    def flight(self): # Method Flight Here Is A Different Result Dislike Flight In Bird
        print("Sparrows can fly!")
# Ostrich child class
class Ostrich(Bird): # Child Class From Bird With Inherit All Method And Attribute
    def flight(self): # Method Flight Here Is A Different Result Dislike Flight In Bird
        print("Ostriches cannot fly!")

bird01 = Bird() # Object From Bird Class
sparrow01 = Sparrow() # Object From Sparrow Class
ostrich01 = Ostrich() # Object From Ostrich Class

bird01.intro() # Hi, there are many types of birds!
bird01.flight() # Most of birds can fly but some cannot!

sparrow01.intro() # Hi, there are many types of birds!
sparrow01.flight() # Sparrows can fly

ostrich01.intro() # Hi, there are many types of birds!
ostrich01.flight() # Ostriches cannot fly!

# Here The Flight method Get A Different Result With Polymorphism Concept
