def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1] 
    smaller = [x for x in arr[:-1] if x <= pivot]  
    greater = [x for x in arr[:-1] if x > pivot] 
    return quicksort(smaller) + [pivot] + quicksort(greater)  


arr = [4, 2, 8, 6, 1, 7, 3, 5]
sorted_arr = quicksort(arr)
print(sorted_arr)

