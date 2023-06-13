class Dog_vocie:
    def voice(self, age):
        if age < 1:
            self.sound = "tyaf"
        elif age < 3:
            self.sound = "gav"
        elif age > 3:
            self.sound = "rrr"
        return self.sound
    
    
print(Dog_vocie().voice(0.5))