class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person's name is {self.name} and age is {self.age}"
    
    def __add__(self, other):
        if isinstance(other, Person):
            return Person(name=f"{self.name} {other.name}", age=self.age + other.age)
        else:
            raise TypeError("Unsupported operand type")
    
    
person1 = Person("Shahll", 19)
person2 = Person("Akane", 16)

# Method __add__

person3 = person1 + person2
print(person3) # Output: Person's name is Shahll Akane and age is 35
