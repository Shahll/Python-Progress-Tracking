def partition(array, low, high):
    wall = low
    pivot = array[high]

    for i in range(low, high):
        if array[i] < pivot:
            array[i], array[wall] = array[wall], array[i]
            wall += 1

    array[high], array[wall] = array[wall], array[high]

    return wall


def median_of_three(array, low, high):
    mid = (low + high) // 2

    if array[mid] < array[low]:
        array[mid], array[low] = array[low], array[mid]
    if array[high] < array[low]:
        array[high], array[low] = array[low], array[high]
    if array[mid] > array[high]:
        array[mid], array[high] = array[high], array[mid]


def quick_sort(array, low, high):
    if low < high:

        median_of_three(array, low, high)

        wall = partition(array, low, high)

        quick_sort(array, low, wall - 1)
        quick_sort(array, wall + 1, high)

# Driver
lst = [12, 1, 77, 34, 8, 56, 6, 17, 28, 39]
quick_sort(lst, 0, len(lst) - 1)
print(lst)
