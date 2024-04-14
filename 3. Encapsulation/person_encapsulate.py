# Setter And Getter In Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name # public Member
        self.__age = age # Private Member

    # getting Method To Get Age
    def get_age(self):
        return self.__age

    # Setting Method To Set Age
    def set_age(self, age):
        self.__age = age

person01 = Person("Ahmed", 35) # Name: Ahmed age 35

# Getting private age for person01
print("Name:", person01.name,"age", person01.get_age())

# Modify age
person01.set_age(36)

print("Name:", person01.name,"age", person01.get_age()) # Name: Ahmed age 36
