array = [4,3,2,10,1,12,8]


for i in range(1,len(array)): # takind index of a number strating at second number
    
    j = i # save an index in this value

    while j > 0 and array[j - 1] > array[j]:   #  work when index not equals 0 or less and 
                                               # when the number previously in the list will not be less than the next
        
        temp = array[j]  # temp value to save number we want ti insert
        
        array[j] = array[j-1]  # normal number is equals previous
        array[j - 1] = temp  # previous number equals temp number

        j = j -1 # decreasing an index
        
        
print(array)