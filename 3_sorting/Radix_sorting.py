def radix_sort(array):
    # Находим максимальное число для определения количества разрядов
    spread = len(str(max(array)))
    temps = []

    # Проходим по каждому разряду
    for div in range(spread):
        
        # Создаем 10 корзин для размещения элементов
        temps = [[] for _ in range(10)]
        # Распределяем элементы в соответствующие корзины
        for num in array:
            # Получаем значение текущего разряда числа
            current_digit = (num // (10 ** div)) % 10
            # Размещаем число в соответствующей корзине
            print(num,current_digit)
            temps[current_digit].append(num)
        # Собираем элементы из корзин и обновляем исходный массив
        array = [num for temp in temps for num in temp]
    # Возвращаем отсортированный массив
    return array
# Driver
lst = [46, 37, 285, 589, 1, 248, 705, 543, 69, 19]
print(radix_sort(lst))
