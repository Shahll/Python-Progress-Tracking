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
            
            
    def remove(self, data):
        current = self.head
        prev = None
        found = False
        
        while current and not found:
            if current.data == data:
                found = True
            else:
                prev = current
                current = current.next
        if current is None:
            return
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

        current.next = None
    
    def find_max(self):
        current = self.head
        highest = current.data
        
        while current:
            if highest < current.data:
                highest = current.data
            else:
                current = current.next
                
        return highest
    
    def del_value(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
                
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(30)
my_list.append(30)
my_list.append(30)
my_list.remove(20)

max_num = my_list.find_max()

my_list.del_value(max_num)

print(my_list.print_list())