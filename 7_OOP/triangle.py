import math

class Angels:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        
    def initialisation(self, side_a, side_b, side_c):
        self.a = int(side_a)
        self.b = int(side_b)
        self.c = int(side_c)
        
        if self.a + self.b + self.c != 180:
            self.a = self.b = self.c = None
            return "There is no such triangle"
        
    def triangle_type(self):
        if self.a == None:
            return f"Please enter the right triangle"
        
        if self.a  == self.b or self.a  == self.c or self.b == self.c:
            return "This triangle is isosceles"
        
        if self.a == self.b == self.c:
            return "This triangle is equilateral"
        
        if self.a != self.b != self.c and self.a != self.c:
            return "This triangle is sided"
        
class Geometry:
    def __init__(self):
        self.side_a = None
        self.side_b = None
        self.side_c = None
        self.height = None
        
    def initialisation(self, side_a, side_b, side_c, height):
        self.side_a = int(side_a)
        self.side_b = int(side_b)
        self.side_c = int(side_c)
        self.height = height
        
    def perimeter(self):
        return self.a + self.b + self.c  
    
    def area(self):
        if self.height is not None:
            user = input("from which side was the height measured? (a/b/c): ")
            if user == 'a':
                return (self.side_a * self.height) // 2
            elif user == 'b':
                return (self.side_b * self.height) // 2
            elif user == 'c':
                return (self.side_c * self.height) // 2
            else:
                return "Invalid input. Please choose either 'a', 'b', or 'c'."
            
        if self.height is None:
            p = (self.side_a + self.side_b + self.side_c) // 2
            print(p)
            temp = p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)
            answer = math.sqrt(temp)
            if answer == 0.0:
                return "The triangle is degenerative"
            else:
                return answer
"""    
a = Angels()
a.initialisation(20,150,10)
print(a.triangle_type())
"""

g = Geometry()
g.initialisation(11, 5, 10, None)
print(g.area())