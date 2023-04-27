
#5. iндекс (розташування, номер по порядку введення) мінімального та максимального числа послідовності
#5. index (location, number in the order of input) of the minimum and maximum sequence numbers



min_number = float("inf")
max_number = float("-inf")
user_input = None
i = -1
while user_input != 0:

    user_input = int(input("Write an integer(enter 0 to stop): "))
    i += 1
    if user_input != 0:
        if min_number > user_input: 
                min_number = user_input
                min_index = i
        
        if max_number < user_input:
                max_number = user_input
                max_index = i


print(f"max = {max_number} and max number index is {max_index} \nmin = {min_number} and min number index is {min_index}")


