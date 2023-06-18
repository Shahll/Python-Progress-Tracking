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
    
    
    def length(self):
        l = 0
        current = self.head
        while current:
            current = current.next
            l += 1
        return l    
    
    
    def del_first_mid_last(self):
        last = my_list.length() - 1
        mid = last // 2
        count = 1
        prev = None
        current = self.head
        
        self.head = current.next
        current = current.next

        while current:
            if count == mid or count == last:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
            prev = current
            current = current.next    
            count += 1
    
            
    
    
    
my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)

print(my_list.print_list())
my_list.del_first_mid_last()
print(my_list.print_list())