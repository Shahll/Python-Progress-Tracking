def shell_sort(array):
    n = len(array)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
                array[j] = temp

            gap = gap // 2

    return array


lst = [79, 28, 3, 7, 93, 55, 1, 0, 27, 69]
print(shell_sort(lst))
