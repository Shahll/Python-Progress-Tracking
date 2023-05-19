def flip(array,index):
    array[:index + 1 ] = array[:index + 1] [::-1]
    return array


def maximal_index(array,index):
    maximal_index = 0
    for i in range(1, index):
        if array[i] > array[maximal_index]:
            maximal_index = i
    return maximal_index


def pancake_sort(array):
    l = len(array)
    for remain in range(l, 1, -1):
        max_indx = maximal_index(array, remain)
        if max_indx != remain - 1:
            flip(array,max_indx)
            flip(array,remain - 1)
    return array
                     
# Driver       
lst = [3, 5, 2, 1, 7, 6, 4]
print(pancake_sort(lst))
