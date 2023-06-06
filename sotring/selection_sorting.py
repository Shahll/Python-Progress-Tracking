def selection_sort(array):
    n = len(array)
    
    for i in range(n):
        min_index = i
        for j in range(i, n ):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index]  = array[min_index] , array[i]
        
    return array
# Driver  
lst = [1,3,6,-1,0,34,7,0,123,9]     
print(selection_sort(lst))
