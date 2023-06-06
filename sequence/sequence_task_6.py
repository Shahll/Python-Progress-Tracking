#6. Кількість максимальних та мінімальних чисел у послідовності
#6. The number of maximum and minimum numbers in the sequence



min_number = float("inf")
max_number = float("-inf")
user_input = None

quanlity_min = 0
quanlity_max = 0

while user_input != 0:

    user_input = int(input("Write an integer(enter 0 to stop): "))

    if user_input != 0:
        if min_number > user_input: 
                min_number = user_input
                quanlity_min = 0
        if max_number < user_input:
                max_number = user_input
                quanlity_max = 0

        print(quanlity_max, quanlity_min)
        

        if min_number == user_input: 
            
                quanlity_min += 1

        if max_number == user_input:
            
                quanlity_max += 1


print(f"quanlity of max numbers = {quanlity_max} \nquanlity of min numbers = {quanlity_min}")  
