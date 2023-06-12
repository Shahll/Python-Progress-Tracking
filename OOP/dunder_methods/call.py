class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __call__(self):
        return f"{self.name} is {self.age} years old"
    
    
person = Person("Shahll", 19)

# Method __call__
# You can run object as a function

print(person()) # Output: Shahll is 19 years old