# Example To Class
class Snake: # New Class Name Snake
    """Snake main blueprint""" # Similar To Comment To Description Class
    name = "Anaconda" # Name Attribute In All Instance From Snake Class

    # Method to change name
    def modifyName(self, new_name):
        self.name = new_name

# Objects based on Snake
snake01 = Snake()

# printing on screen
print(snake01.name) # Anaconda

# Modify the name using modifyName Method
snake01.modifyName("Python") # Redeclare To Name Attribute
print(snake01.name) # Python

# Using Dunder init and instance attributes
class Snake:
    """Snake main blueprint"""
    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName

# Objects
anaconda01 = Snake("Anaconda") # With Dunder Init To Set Name
python01 = Snake("Python") # With Dunder Init To Set Name

# printing the value of name for the two objects
print(anaconda01.name) # Anaconda
print(python01.name) # Python
