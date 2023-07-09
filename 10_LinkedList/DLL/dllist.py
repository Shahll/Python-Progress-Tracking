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
    def __lt__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for <: Dllist expected" + self.CEND)
        return len(self) < len(other)
    #
    #
    def __le__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for <=: Dllist expected" + self.CEND)
        return len(self) <= len(other)
    #
    #
    def __eq__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for ==: Dllist expected" + self.CEND)
        
        current = self._head
        current_other = other._head
        while current and current_other:
            if current_other.data != current.data:
                return False
            current = current.next
            current_other = current_other.next
        if current_other is None and current is not None:
            return False
        if current is None and current_other is not None:
            return False
        return True
    #
    #
    def __ne__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for !=: Dllist expected" + self.CEND)
        
        current = self._head
        current_other = other._head
        while current and current_other:
            if current_other.data != current.data:
                return True
            current = current.next
            current_other = current_other.next
        if current_other is None and current is not None:
            return True
        if current is None and current_other is not None:
            return True
        
        return False
    #
    #
    def __repr__(self):    
        if self._head is None:
            return 0
        count = 0
        current = self._head
        while current:
            count += 1
            current = current.next
        return str(count)
    #
    #
    def __gt__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for >: Dllist expected" + self.CEND)
        return len(self) > len(other)
    #
    #
    def __ge__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for >=: Dllist expected" + self.CEND)
        return len(self) >= len(other)
    #
    #
    def bool(self):
        return False if self._head is None else True
    #
    #
    def __mul__(self, intiger):
        if isinstance(intiger, int):
            base_list = self.copy()
            for _ in range(intiger):
                for item in base_list:
                    self.append(item.data)
            return self
        else:
            raise TypeError(self.CRED + "Unsupported operand type for *: int expected" + self.CEND)
    #
    #
    def __iadd__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for +=: Dllist expected" + self.CEND)
        if self._head is None:
            self._head = other._head
            
        if other._head is not None:
            current_other = other._head
            while current_other:
                self.append(current_other.data)
                current_other = current_other.next
        return self
    #
    #
    def __radd__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for +: Dllist expected" + self.CEND)
        if self._head is None:
            self._head = other._head
            
        if other._head is not None:
            current_other = other._head
            while current_other:
                self.append(current_other.data)
                current_other = current_other.next
        return self
    #
    #
    def __add__(self, other):
        if not isinstance(other, Dllist):
            raise TypeError(self.CRED + "Unsupported operand type for +=: Dllist expected" + self.CEND)
        if self._head is None:
            self._head = other._head
            
        if other._head is not None:
            current_other = other._head
            while current_other:
                self.append(current_other.data)
                current_other = current_other.next
        return self
    #
    #
    def __getitem__(self, index):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        
        if index < 0:
            index = self._length + index
        if index < 0:
            index = 0
        if index >= self._length:
            index = self._length
        remain = 0
        current = self._head
        while remain < index:
            remain += 1
            current = current.next
        return current.data
    #
    #
    def __setitem__(self, index, item):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        
        if index < 0:
            index = self._length + index
        if index < 0:
            index = 0
        if index >= self._length:
            index = self._length
        remain = 0
        current = self._head
        while remain < index:
            remain += 1
            current = current.next
        current.data = item
    #
    #
    def __delitem__(self, index):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        
        if index < 0:
            index = self._length + index
        if index < 0:
            index = 0
        if index >= self._length:
            index = self._length
        self.pop(index)
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
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        if index < 0:
            index = self._length + index
        if index < 0:
            index = 0
            
        if self._length <= index:
            index = self._length
        
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
            current.next.prev = new_node
            current.next = new_node
                    
        self._length += 1
    #
    #
    def pop(self, index=None):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        if index == None:
            index = self._length - 1
        else:
            if index < 0:
                index = self._length + index
            if index < 0:
                raise IndexError(self.CRED + "Index out of the range" + self.CEND) 
            if index >= self._length:
                raise IndexError(self.CRED + "Index out of the range" + self.CEND) 
        
        if self._head.next is None:
            self._head = None
            self._tail = None
            self._length = 0
        
        current = self._head
        remain = 0
        while remain < index:
            remain += 1
            current = current.next
        
        if current.prev is None:
            current.next.prev = None
            self._head = current.next
        
        elif current.next is None:
            current.prev.next = None
            self._tail = current.prev
        else:
            current.next.prev = current.prev
            current.prev.next = current.next
            

            
        self._length -= 1
        return current.data
    #
    #
    def to_set(self):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        lst = []
        current = self._head
        while current:
            if current.data not in lst:
                lst.append(current.data)
            current = current.next
        return lst
    #
    #
    def filter_list(self, condition):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        while current:
            if not condition(current.data):
                if current.prev is None:
                    current.next.prev = None
                    self._head = current.next
                elif current.next is None:
                    current.prev.next = None
                    self._tail = current.prev
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                self._length -= 1
            current = current.next
    #
    #
    def reverse(self):
        if self._head is None or self._head.next is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        previous = None
        temp = None
        while current:
            temp = current.next 
            current.next = previous 
            previous = current 
            current = temp 
        self._tail = self._head
        self._head = previous
    #
    #
    def shift(self, direction, times):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        if direction == "left":
            for _ in range(times):
                self.append(self.pop(0))
        elif direction == "right":
            for _ in range(times):
                self.prepend(self.pop())
        else:
            raise TypeError(self.CRED + "Unsupported variable : 'left' or 'right' expected" + self.CEND)
    #
    #
    def copy(self):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        copy = Dllist()
        current = self._head
        while current:
            copy.append(current.data)
            current = current.next
        return copy
    #
    #
    def sort(self):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        string = str(self)[1:-1]
        lst = []
        for char in string.split(", "):
            lst.append(int(char))
        lst = sorted(lst)
        d.clear()
        for num in lst:
            d.append(num)
    #
    #
    def reduce_list(self):
        if self._head is None:
            raise IndexError(self.CRED + "DLL is empty" + self.CEND)
        current = self._head
        summ = 0
        while current:
            summ += current.data
            current = current.next
            
        return summ
if __name__ == "__main__":
    d = Dllist()
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)

    
print(f"List - {d}  length - {len(d)}  tail - {d._tail.data if d._tail is not None else d._tail}  "
       f"head - {d._head if d._head is None else d._head.data}")

    
            
