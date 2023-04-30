#1. Знайти максимальне число у масиві
     
array = [3,4,2,7]

highest = array[0]

for num in array:
    if highest < num:
        highest = num
        
print(highest)
