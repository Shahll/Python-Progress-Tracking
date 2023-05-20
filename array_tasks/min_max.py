"""
Знайти максимальне число у списку
Знайти мінімальне число у списку 
""" 

def min_max_number(array):
    max_num = min_num = array[0]
    for number in array:
        if max_num < number:
            max_num = number
        elif min_num > number:
            min_num = number
    return max_num, min_num

# Driver
lst = [4, 2, 3, 2, 2, 4, 7, 7, 9, 9, 9, 1, 1]
print(min_max_number(lst))
