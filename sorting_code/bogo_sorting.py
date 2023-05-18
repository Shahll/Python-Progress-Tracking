import random

array = [1, 2, 3, 1, 5, 6,4,42,]

flag = True
i = 0 # step counter

while array != sorted(array):
    i += 1
    a,b = random.randint(0,len(array) -1 ),random.randint(0,len(array)-1)
    array[a], array[b] = array[b], array[a]
    
    
print(f"Sorted array is {array}\n it took {i} steps")