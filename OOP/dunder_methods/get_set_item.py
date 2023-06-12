class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __getitem__(self, index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.age
        else:
            raise IndexError("Index out of range")
        
    def __setitem__(self, index, value):
        if index == 0:
            self.name = value
        if index == 1:
            self.age = value
        else:
            raise IndexError("Index out of range")
        
        
person = Person("Shahll", 19)

# Methods __getitem__ and __setitem__

print(person[0]) # Output: Shahll
person[1] = person[1] + 1
print(person[1]) # Output: 20

