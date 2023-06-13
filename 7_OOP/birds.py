
""" 
У нас є три птахи 

Пенгвін
 - Може ходити 
 - Може плавати 
Страус
 - Може ходити
 - може бігти 
 - може засунути голову у пісок 
Сокіл 
 - може ходити 
 - може літати 
"""

class Bird:
    def __init__(self):
        self.head = None
        self.legs = None
        self.wings = None
        self.tail = None
        
    def walking(self):
        pass
    
    def exist(self):
        pass
    
    def eating(self):
        pass
    
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        
    def swimming(self):
        pass
    
class Ostrich(Bird):
    def __init__(self):
        super().__init__()
        
    def running(self):
        pass
    
    def hide_head_in_sand(self):
        pass
    
class Hawk(Bird):
    def __init__(self):
        super().__init__()
        
    def flying(self):
        pass
    
