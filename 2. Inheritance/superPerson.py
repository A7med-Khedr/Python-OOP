# multiple Inheritance 
class Person: # Person Parent Class
    def person_data(self, name, age): # Function To Set Name And Age
        print("Hello from the Person class!")
        print("the name is:", name,"and the age is:", age)

class Company: # Company Parent Class
    def company_data(self, comp_name, location):
        print("Welcome to the company!")
        print("The company name is:", comp_name, "and location is:", location)

class Employee(Person, Company): # Employee Child Class And Inherit All Method And
    # Attribute In Person And Company Classes
    def employee_data(self, salary, skill):
        print("Welcome to the Employee class")
        print("Salary is:", salary, "Skill is:", skill)

emp01 = Employee() # Objects for Employee

emp01.person_data("Ronaldo", 35) # Access Data in Person Class
emp01.company_data("ABCD", "location001") # Access Data in Company Class
emp01.employee_data(10000, "Data Science") # Access Data in Employee Class
