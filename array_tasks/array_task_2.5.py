"""2.5 рівень__________
 а. Визначити, чи число парне ( ділиться на 2 )   
 б. Визначити, чи є число простим ( повинне ділитися лише на себе )
 с. порахувати розряди числа
 """
 

array = [1, 2, 3, 0, 4, 5, 6, 1, 2, 6, 0]

for number in array:
    if number %2 == 0:
        if number != 0:
            print(number,"is pair number")
            
            



array = range(0,100)
check = [2,3,5,7]

prime = []
for num in array:
    for divisor in check:
        if num %divisor == 0 and num != divisor:
            break
    else: 
            prime.append(num)
print(f"\nthis numbers are prime: {prime}\n")



number = 123456
counter = 1
flag = True
while flag == True:
    if number / 10 > 1:
        counter += 1
        number = number / 10
    else:
        flag = False
print(f"your number have {counter} discharges")