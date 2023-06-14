class alive:
    def __init__(self):
        self._growth = 0
        self._is_watered = False
        self._alive = True
        
    def get_growth(self):
        return self._growth

    def set_growth(self, value):
        self._growth = value
    
    def get_is_watered(self):
        return self._is_watered

    def set_is_watered(self, value):
        self._is_watered = value
    
    def get_alive(self):
        return self._alive

    def set_alive(self, value):
        self._alive = value
        
class not_alive:
    def __init__(self):
        self._material = ""
        self._count = 0
        
    def get_material(self):
        return self._material
    
    def set_material(self, value):
        self._material = value
        
    def get_count(self):
        return self._count
    
    def set_count(self, value):
        self._count = value

class grass(alive):
    def __init__(self):
        super().__init__()
        
    def watering(self):
        print("Oh yeaaah imma grass and I am wet ")
    
    def __str__(self):
        return "Grass"

class tulip(alive):
    def __init__(self):
        super().__init__()
        
    def watering(self):
        print("I'm royalty, pour champagne on me, not water ")
    
    def __str__(self):
        return "Tulip"

class rock(not_alive):
    def __init__(self):
        super().__init__()
        
class bench(not_alive):
    def __init__(self):
        super().__init__()

class garden:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def __str__(self):
        return f"In the garden: {', '.join(str(obj) for obj in self.objects)}"
        
    
    def water(self):
        for obj in self.objects:
            obj.watering()
    

g = garden()

grass = grass()
tulip = tulip()

g.add_object(grass)
g.add_object(tulip)

g.water()
print(g)
