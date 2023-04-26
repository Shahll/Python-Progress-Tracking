with open("task_one.txt", "w+") as file:
    user_input = ''
    while True:
        x = input("Write an integer (enter 0 to stop): ")
        if x == '0':
            break
        user_input += x + ','
    file.write(user_input.strip())

 
with open("task_one.txt", "r") as file:
    user_input = [int(x) for x in file.read().split(',')]
    user_input.sort()
    print(user_input)
