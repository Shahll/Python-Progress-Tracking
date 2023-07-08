from node import Node

class Dllist:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
        self.CRED = '\033[91m'
        self.CEND = '\033[0m'
    #   
    #   
    def __str__(self):
        if self._head is None:
            return "[]"
        else:
            arr = []
            current = self._head
            while current:
                arr.append(str(current.data))
                current = current.next
            return "[" + ", ".join(arr) + "]"
    #
    #   
    def __len__(self):
        return self._length
    #    
    #    
    def __iter__(self):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        while current:
            yield current
            current = current.next
    #
    #
    def prepend(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._length += 1
    #    
    #    
    def append(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
        self._tail = new_node
        self._length += 1
    #    
    #   
    def append_after(self, AfterValue, item):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        new_node = Node(item)
        current = self._head
        while current and current.data != AfterValue:
            current = current.next
            
        if current is None:
            raise ValueError(self.CRED + "AfterValue is not in the DLL" + self.CEND)
        if current.next is None:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        else:
            current.next = new_node
            new_node.prev = current
        self._length += 1
    #
    #      
    def append_before(self, BeforeValue, item):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        new_node = Node(item)
        while current:
            if current.data == BeforeValue:
                break
            current = current.next
            
        if current is None:
            raise ValueError(self.CRED + "BeforeValue is not in the DLL" + self.CEND)
        if current.prev is None:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        else:
            new_node.next = current.next
            current.next = new_node
        self._length += 1
    #
    #
    def remove(self, RemoveValue):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        while current:
            if current.data == RemoveValue:
                break
            current = current.next
            
        if current is None:
            raise ValueError(self.CRED + "RemoveValue is not in the DLL" + self.CEND)
        
        if self._length == 1:  # if there is only 1 element
            self._head = None
        
        elif current.prev is None: # if the element in the beggining og the list
            current.next.prev = None
            self._head = current.next
            
        elif current.next is None: # if the element at the end of the list
            current.prev.next = None
            self._tail.prev = current.prev
            self._tail = current.prev
            
        else: # if element have previous node and next node
            current.prev.next = current.next
            current.next.prev = current.prev
            
        self._length -= 1
    #
    #
    def delete(self, index):
        if index < 0:
            index = self._length + index
            if (index < 0):
                raise IndexError(self.CRED + "Index out of the range" + self.CEND)
            
        if self._length <= index:
            raise IndexError(self.CRED + "Index out of the range" + self.CEND)
        
        if index == 0 and self._length == 1:
            self._head = None
            
        elif index == 0:
            self._head.next.prev = None
            self._head = self._head.next
        
        else:        
            current = self._head
            remain = 0
            while current and index != remain:
                remain += 1
                current = current.next
                
            if current is None:
                raise IndexError(self.CRED + "Index out of the range" + self.CEND) 
                
            current.prev.next = current.next
            current.next.prev = current.prev
            
            if index + 1 == self._length:
                self._tail = current
                
        self._length -= 1
    #   
    #
    def remove_all(self, RemoveValue):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        
        if self._length == 1 and self._head == RemoveValue:
            self._head = None
        else:  
            current = self._head
            while current:
                find = False
                find = (current.data == RemoveValue)
                if find:
                    if current.prev is None:
                        current.next.prev = None
                        self._head = current.next
                        
                    elif current.next is None:
                        current.prev.next = current.next
                        self._tail = current.prev
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        
                    self._length -= 1
                current = current.next
    #
    #
    def count(self, CountValue):
        return sum(1 for node in self.__iter__() if node.data == CountValue)
    #
    #
    def length(self):
        return self._length
    #
    #
    def minimal(self):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        min_num = self._head.data
        while current:
            if current.data < min_num:
                min_num = current.data
            current = current.next
            
        return min_num
    #
    #
    def maximal(self):            
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        max_num = self._head.data
        while current:
            if current.data > max_num:
                max_num = current.data
            current = current.next
            
        return max_num
    #
    #
    def clear(self):
        self._head = None
        self._tail = None
        self._length = 0
    #
    #
    def index_of(self, SearchValue):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        index = 0
        while current:
            if current.data == SearchValue:
                break
            index += 1
            current = current.next
        return index
    #
    #
    def is_empty(self):
        return self._head == None
    #
    #
    def insert(self, index, item):
        if index < 0:
            index = self._length + index
        if index < 0:
            index = 0
        elif index > self._length:
            index = self._length
                
        if self._head is None:
            self._head = Node(item)
            self._tail = self._head
        elif index == 0:
            new_node = Node(item)
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        elif index == self._length:
            new_node = Node(item)
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
            
        else:
            current = self._head
            counter = 0
            while counter < index:
                counter += 1
                current = current.next
                
            new_node = Node(item)
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            if index == self._length:
                self._tail = new_node
                    
        self._length += 1
        
        
if __name__ == "__main__":
    d = Dllist()
    d.append(1)
    d.append(2)
    d.append(4)
    d.append(5)

    d.insert(2, 3)
    d.insert(0, 0)
    d.insert(-313, -1)
    d.insert(3131, 6)
    


    
print(f"List - {d}  length - {len(d)}  tail - {d._tail.data if d._tail is not None else d._tail}  "
       f"head - {d._head if d._head is None else d._head.data}")

    
            
