# Abstraction
from abc import ABC, abstractmethod # abc Is A Library In Python
# Abc To Make Abstract Classes
# abstractmethod Tool To decorate Method Inside Class
class AbsClass(ABC): # Abstract Class Can Not Make Instance From Here directly
    # Its Role is to Provide a Form for other Classes
    def print(self, x):
        print("Inserted value: ", x)
    @abstractmethod # To Define Abstract Method
    def task(self):
        print("Hi, we are inside AbsClass task")
        # Don't Make Any Thing But Must Define This Method In All Instance To Make A Task
        # Because It Is A Abstract Method

# test child class
class test_class(AbsClass): # Child Class From AbsClass
    def task(self): # Initialization task Method To Make A Task
        print("Hi, we are inside test_class task")

# example child class
class example_class(AbsClass): # Child Class From AbsClass
    def task(self): # Initialization task Method To Make A Task
        print("Hi, we are inside example_class task")

# Objects of test_class
test01 = test_class() # Object From test_class
test01.task() # Hi, we are inside test_class task
test01.print(50) # Inserted value:  50

# Object of example_class
example01 = example_class() # Object From example_class
example01.task() # Hi, we are inside example_class task
example01.print(150) # Inserted value:  150

# Testing
print("test01 is instance of AbsClass? ", isinstance(test01, AbsClass))
# test01 is instance of AbsClass?  True
print("example01 is instance of AbsClass? ", isinstance(example01, AbsClass))
#  example01 is instance of AbsClass?  True
# isinstance Method Return ( True | False ) To test01 And example01 Is Instance From AbsClass Or No
