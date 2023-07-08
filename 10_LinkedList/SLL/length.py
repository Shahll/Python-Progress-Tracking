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
  
        
        
    def length(self): 
        l = 0
        current = self.head
        while current.next:
            current = current.next
            l += 1
        print(f"Length of the list is {l}")