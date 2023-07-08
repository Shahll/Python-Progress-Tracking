class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data): 
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(current.data)
            current = current.next
  
        
    
    def remove(self, data):
        current = self.head
        previous = None
        found = False
        
            
        while current and not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            return
        
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
            
            
        current.next = None

