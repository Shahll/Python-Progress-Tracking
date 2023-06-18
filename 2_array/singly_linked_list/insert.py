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
  
    
    def insert(self, data, index):
        new_node = Node(data)
        
        if index < 0:
            print("Invalid index")
            
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        previous = None
        current_index = 0
        
        while current_index < index and current:
            prev = current
            current = current.next
            current_index += 1
            
        if current_index < index:
            print("Invalid index")
    
        prev.next = new_node
        new_node.next = current
    
