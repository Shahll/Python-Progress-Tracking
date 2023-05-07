user = int(input("enter the number to see the closest Fibonacci number to it: "))

first_num = 0
second_num = 1

answer = 0

count = 1 
for i in range(0,user):
    count += 1
    
    if count % 2 == 0: 
        first_num = first_num + second_num
        answer = first_num
    else:
        second_num = first_num + second_num
        answer = second_num
        
        
    if first_num >= user or second_num >= user:
        
        if abs(first_num - user) < abs(second_num - user):
        
            print(f"the highest fibomacci number that high or equels your number is {first_num}")
            break
        else:
            print(f"the highest fibomacci number that high or equels your number is {second_num}")