
def insertion_sort(array):
    for i in range(1,len(array)): 
        j = i 
        while j > 0 and array[j - 1] > array[j]:  
            temp = array[j]
            array[j] = array[j-1]  
            array[j - 1] = temp
            j = j -1 
    return array
# Driver     
lst  = [4,3,2,10,1,12,8]
print(insertion_sort(lst))
