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
        
        
    def search_by_value(self, data): #  search_by_value
        current = self.head
        l = 1
        while current.data != data:
            current = current.next
            l += 1
        print(f"Value is on {l} position")
        
        
    def search_by_index(self, index): #  search_by_index
        current = self.head
        i = 0
        while i != index:
            current = current.next
            i += 1
        print(f"On the {index} index is {current.data}")

    
    def insert(self, data, index):
        new_node = Node(data)
        
        if index < 0:
            print("Invalid index")
            
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        current_index = 0
        
        while current_index < index and current:
            prev = current
            current = current.next
            current_index += 1
            
        if current_index < index:
            print("Invalid index")
    
        prev.next = new_node
        new_node.next = current
    
    
    def remove(self, data):
        current = self.head
        previous = None
        
            
        while current:
            if current.data == data:
                break
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
    
    
    def clear(self):
        self.head = None 
        
        
    def merge(self, second_list):
        if self.head is None:
            self.head = second_list.head
            return

        if second_list.head is None:
            return

        current = self.head
        while current.next:
            current = current.next
            
        current.next = second_list.head
        
        second_list.head = None
    
    
    
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)



#my_list.length()

#my_list.search_by_value(20)

#my_list.search_by_index(2)

my_list.clear()

#my_list.remove(10)

#my_list.insert(12, 2)

#my_list.merge(list2)

my_list.print_list()
