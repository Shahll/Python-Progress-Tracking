import random
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = random.randint(0, 1000)
        self.courses = []
        
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
    
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            
    def get_course(self):
        return [i for i in self.courses]
    
    def get_student(self):
        return f"Your name is {self.name}, your age is {self.age} and your id is {self.id}"
    
    
st = Student("Shahll", 19)

st.add_course("English")
st.add_course("German")
st.add_course("Java")

print(st.get_course())
print(st.get_student())


