""" 
Видалити зі списку всі максимальні та мінімальні елемент 
"""
def min_max_number(array):
    max_num = min_num = array[0]
    for number in array:
        if max_num < number:
            max_num = number
            
        elif min_num > number:
            min_num = number
    return max_num,min_num


def del_min_max(array,min_num,max_num):
    n = 0
    while n != len(array):
        for delete in array:
            if delete == min_num or delete == max_num:
                array.remove(delete)
        n += 1
    return array


lst =[4,2,3,2,2,4,7,7,9,9,9,1,1]
max_num, min_num = min_max_number(lst)

print(del_min_max(lst,min_num,max_num))