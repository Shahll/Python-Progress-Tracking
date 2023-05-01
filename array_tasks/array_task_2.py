"""2 рівень  __________
 а. Порахувати кількість нулів, максимальних та мінімальних чисел у списку
    [ 1, 2, 3, 0, 4, 5, 6, 1, 2, 6] -> 1, 2, 2 
 б. Є початкове число та список. Знайти у списку це число помножене на 2 та повернути його індекс 
  2, [ 1, 2, 3, 4, 5] -> 3 
 в. Знайти число у списку яке найбільше повторюється. 
    [ 1, 1, 1, 2, 2, 4, 4, 4, 4, 4] -> 4 
    """
    

array = [ 1, 2, 3, 0, 4, 5, 6, 1, 2, 6, 0]



zero_counter = 0
for numbers in array:
    if numbers == 0:
        zero_counter += 1
        
        
minimal_number = array[0]
minimal_counter = -1
for numbers in array:
    if minimal_number > numbers:
        minimal_number = numbers
      
    if numbers == minimal_number:
        minimal_counter += 1


maximal_number = array[0]
maximal_counter = -1
for numbers in array:
    if maximal_number > numbers:
        miximal_number = numbers
      
    if numbers == maximal_number:
        maximal_counter += 1

print("array:", array)
print(f"Number of maximal numbers is: {maximal_counter}")
print(f"Number of minimal numbers is: {minimal_counter}")
print(f"Number of zero's is: {zero_counter}\n") 



    
array = [1, 2, 3, 0, 4, 5, 6, 1, 2, 6, 0]
search = 2 * 2  

for number in range(len(array)):
    if array[number] == search:
        print(f"array: {array}\nindex of {search} is {number}\n")
        break

        

array = [1, 1, 1, 2, 2, 4, 4, 4, 4, 4, 4 ]

#как я понял мы смотрим какое самое большое число в отсортрованном листе тоесть единица была 3 раза двойка 2 раза и 4 пять раз
# и мах смотрит какого числа больше всего
most_common_number = max(set(array), key = array.count)

print(f"array: {array}\nmost common number in array is: {most_common_number}")