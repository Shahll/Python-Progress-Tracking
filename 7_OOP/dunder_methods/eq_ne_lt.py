class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        else:
            raise TypeError("Unsupported operand type")
    
    

person1 = Person("Shahll", 19)
person2 = Person("Akane", 16)

# Methods __eq__, __ne__, and __lt__

print(person1 == person2)  # Output: False
print(person1 != person2)  # Output: True
print(person1 < person2)  # Output: False

