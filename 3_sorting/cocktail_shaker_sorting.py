def cocktail_shaker_sort(array):
    left = 0
    right = len(array) - 1

    while left < right:
        for i in range(left, right):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        right -= 1

        for i in range(right, left, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]

        left += 1

    return array
# Driver
lst = [25, 12, 46, 8, 33, 18, 40, 3, 21, 49, 3]
print(cocktail_shaker_sort(lst))
