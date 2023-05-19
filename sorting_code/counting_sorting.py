def counting_sort(list):
    counting_list = [0] * 10
    for num in list:
        counting_list[num] += 1
    return [index for index, count in enumerate(counting_list) for _ in range(count)]
# Driver
lst = [7, 3, 9, 1, 5, 5, 2, 7, 1, 3, 7, 5, 9, 5]
print(counting_sort(lst))
