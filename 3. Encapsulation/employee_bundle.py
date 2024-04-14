# Encapsulation
# With Access Modifier ( Public, Private, Protect )
# It Is A Container To Collect Information To Make It:
# [1] Security
# [2] Data Hiding
# [3] Simplicity
# [4] Maintainable
class Employee:
    # class constructor
    def __init__(self, name, salary, project):
        self.__name = name # Private Attribute With ( __ ) Access In Class Only
        self._salary = salary # Protect Attribute With ( _ ) Access In Class And Instance
        self.project = project # Public Attribute To Access In ALl Place

    # show the employee data
    def show_details(self): # Method To Get A Private Attribute ( Name ) And ( Salary )
        print("The name is:", self.__name, "And Salary is:", self._salary)

    # Working project
    def work(self):
        print(self.__name, "is working on", self.project)
    
# Objects for employee
employee01 = Employee("Ahmed", 9000, "Video Game")

# Access public name
# print("The value of name is:", employee01.__name)
# # call the public methods for details
employee01.show_details() # The name is: Ahmed And Salary is: 9000 
employee01.work() # Ahmed, is working on, Video Game
