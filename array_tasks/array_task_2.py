#3. Видалити з масиву всі максимальні та мінімальні елемент 
#( Використовувати min, max не можна )

array = [4,2,3,2,2,4,7,7,9,9,9,1,1]
original_array = array.copy() 

min_number = array[0]
            
for min in array:
    if min_number > min:
            min_number = min
            
        
  
for i in array:
    
    for i in array:
        
        if i == min_number:
            array.remove(min_number)
           


max_number = array[0]
            
for max in array:
    if max_number < max:
            max_number = max
            
        
  
for j in array:
    
    for j in array:
        
        if j == max_number:
            array.remove(max_number)
            
print(f"Before {original_array}\nAfter {array}")