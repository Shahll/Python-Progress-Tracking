def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
# Driver
lst = [17, 0, 8, 20, 12, 13, 2, 4,]
print(bubble_sort(lst))
