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
            return None
        lst = []
        current = self.head
        while current:
            lst.append(current.data)
            current = current.next
            
            
        return lst
    
    def del_every_second(self):
        i = -1
        current = self.head
        prev = None
        
        while current:
            if i % 2 == 0:
                prev.next = current.next
            i += 1
            prev = current
            current = current.next
        
        
    
    
    
    
    
    
my_list = LinkedList()

my_list.append(1)
my_list.append(2) # 
my_list.append(3)
my_list.append(4) #
my_list.append(5)
my_list.append(6) #
my_list.append(7)


my_list.del_every_second()
print(my_list.print_list())