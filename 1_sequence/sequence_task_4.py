#4. Мінімальне та максимальне числа послідовності
#4. Minimum and maximum numbers of the sequence


min_number = float("inf")
max_number = float("-inf")
user_input = None

while user_input != 0:

    user_input = int(input("Write an integer(enter 0 to stop): "))

    if user_input != 0:
        if min_number > user_input: 
                min_number = user_input
        
        if max_number < user_input:
                max_number = user_input


print(f"max = {max_number} and min = {min_number}")