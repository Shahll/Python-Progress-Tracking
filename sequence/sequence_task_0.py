"""
 ! Послідовність чисел повинна закінчуватись 0. 
 ! Останнє число не повинно бути числом, яким закінчується послідовність. 
 ( тобто, у послідовності 1 2 3 4 0 останнє число, яке буде враховуватись для завдань - 4 ) 
 ! Ввід та вивід у консолі 

 ! The sequence of numbers must end in 0. 
 ! The last number must not be the number that ends the sequence. 
 (i.e., in the sequence 1 2 3 4 0, the last number to be considered for the problems is 4) 
 ! Input and output in the console
"""




numbers = []
while True:
    x = int(input("Введіть число (введіть 0 для завершення): "))
    if x == 0:
        break
    numbers.append(x)

last_number = numbers[-1]
print("Останнє число в послідовності: ", last_number)
