def partition(array, low, high):
    wall = low
    pivot = array[high]

    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[wall] = array[wall], array[i]
            wall += 1

    array[high], array[wall] = array[wall], array[high]

    return wall





def quick_sort(array, low, high):
    if low < high:
      
        wall = partition(array, low, high)

        quick_sort(array, low, wall - 1)
        quick_sort(array, wall + 1, high)

# Driver
lst = [12, 1, 77, 34, 8, 56, 6, 17, 28, 39]
quick_sort(lst, 0, len(lst) - 1)
print(lst)
