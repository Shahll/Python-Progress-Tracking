class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person's name is {self.name} and age is {self.age}"
    
    def __str__(self) -> str:
        return f"Person's name is {self.name} and age is {self.age}"
    

person1 = Person("Shahll", 19)
person2 = Person("Akane", 16)


# Methods __str__ and __repr__

print(str(person1))  # Output: Person's name is Shahll and age is 19
print(repr(person1))  # Output: Person's name is Shahll and age is 19

print(str(person2))  # Output: Person's name is Akane and age is 16
print(repr(person2))  # Output: Person's name is Akane and age is 16