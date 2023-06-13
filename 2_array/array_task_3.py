"""3 рівень  __________
 а. Видалити з масиву перше, середнє та останнє значення і вивести їх. 
 б. Випадковим чином перемішати список 
 в. Видалити кожен другий елемент списку
    [ 1, 2, 3, 4, 5, 6] -> [ 1, 3, 5 ]
 г. Видалити конкретне число або числа зі списку 
    1, [ 1, 2, 1, 2, 3, 4, 5 ] -? [ 2, 2, 4, 5, 4 ]
"""

"""array = [1,2,3, 4 ,5,6,7]


array.pop(len(array)//2)  
array.pop(array[0])
array.pop()

print(array)
"""


"""import random
array = [1,1,2,2,3,4,4] # this is our list we want to schuffle
shuffled_list = [] # this will be our shuffled list
generated = set() # Here we save all numbers that was print by random

while len(generated) != len(array):
    for i in array:
        index = random.randint(0,len(array) - 1)
        if index not in generated: 
            shuffled_list.append(array[index]) # add to the list number
            generated.add(index) # add to set() number so that it never repeat
        
    
    
        
print(shuffled_list)
"""


"""# в. Видалити кожен другий елемент списку
#    [ 1, 2, 3, 4, 5, 6] -> [ 1, 3, 5 ]

array = [1,2,3,4,5]
array = array[::2]

print(array)"""


"""
# г. Видалити конкретне число або числа зі списку 
#    1, [ 1, 2, 1, 2, 3, 4, 5 ] -? [ 2, 2, 4, 5, 4 ]
 
baseArray = [1,2,3,1,1] #list i want to clear

removeArray = [1,1,2] # numbers we want to remove from Base list

for base in baseArray:
    for remove in removeArray:
        if base == remove: # if number from first list equals number from second list remove this numbers from both lists
            baseArray.remove(remove)
            removeArray.remove(remove)
            break 
        
print(baseArray)

"""
