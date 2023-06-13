class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f"Person's name is {self.name} and age is {self.age}"
        
    def __len__(self):
        return len(self.name)
    
    
person = Person("Shahll", 19)

# Method __len__

print(len(person)) # Output: 6