"""  
Порахувати кількість нулів, максимальних та мінімальних чисел у списку
[ 1, 2, 3, 0, 4, 5, 6, 1, 2, 6] -> 1, 2, 2 
"""


def counter(array):
    zero_count = 0
    min_count = 0
    max_count = 0
    max_num = min_num = array[0]

    for number in array:
        if max_num < number:
            max_count = 1
            max_num = number
        elif max_num == number:
            max_count += 1
        if min_num >= number:
            min_count = 1
            min_num = number
        elif min_num == number:
            min_num += 1
        if number == 0:
            zero_count += 1



    return zero_count, min_count, max_count

# Driver
lst = [1, 2, 3, 0, 4, 5, 6, 1, 2, 6]
print(counter(lst))

