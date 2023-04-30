#2. Знайти мінімальне число у масиві

array = [3,4,2,7]

min_number = array[0]

for num in array:
    if min_number > num:
        min_number = num
        
print(min_number)