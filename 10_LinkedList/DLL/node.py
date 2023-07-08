class Node:
    def __init__(self, data, newNext=None, newPrev=None):
        self.data = data
        self.next = newNext
        self.prev = newPrev
    
    @property
    def prev(self):
        return self._prev
    
    @prev.setter
    def prev(self, newPrev):
        self._prev = newPrev
        
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, newNext):
        self._next = newNext
