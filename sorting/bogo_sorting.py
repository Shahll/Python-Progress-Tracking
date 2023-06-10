import random

def bogo_sort(array):
    while array != sorted(array):
        a,b = random.randint(0,len(array) -1 ),random.randint(0,len(array)-1)
        array[a], array[b] = array[b], array[a]
    return array
# Driver
lst = [1, 2, 3, 1, 5, 6,4,42,]
print(bogo_sort(lst))
