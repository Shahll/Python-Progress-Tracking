array = [1,3,6,-1,0,34]
# -1 0 1 3 6 34


for index, value in enumerate(array):
    for count, item, in enumerate(array):
        if value < item:
            array[index],array[count] = array[count], array[index] 
    
        
print(array)