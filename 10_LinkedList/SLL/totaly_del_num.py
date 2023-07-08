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
    
    def del_all_number(self, num):
        current = self.head
        prev = None
        
        while current:
            if current.data == num:
                if prev is None:
                    self.head = current.next
                    current = self.head
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
my_list.append(10)
my_list.append(10)
my_list.append(10)

my_list.del_all_number(10)

print(my_list.print_list())