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
            
    def find_min(self):
        current = self.head
        temp = current.data
        
        while current:
            if current.data < temp:
                temp = current.data
            current = current.next
        return temp
        
        
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(6)

my_list.find_min()

