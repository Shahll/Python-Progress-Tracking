def selection_sort(array):
    for index, value in enumerate(array):
        for count, item, in enumerate(array):
            if value < item:
                array[index],array[count] = array[count], array[index] 
    return array
# Driver  
lst = [1,3,6,-1,0,34]     
print(selection_sort(lst))
