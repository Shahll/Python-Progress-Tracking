def quick_sort(array):
    pivot = array[len(array) -1]
    wall = 0
    temp = None
    while array != sorted(array):
        for i in range(1,len(array)-1):
            if array[i] < pivot:
                array[wall], array[i] = array[i], array[wall]
                wall += 1
                print(f"wall is {wall}\narray is {array}\nindex is {i}\n")
            if i == len(array)-1:
                array.insert(wall,pivot)
                pivot = array[len(array) -1]
    return array
    
    
lst = [12, 1, 77, 34, 8, 56, 6, 17, 28, 39]
print(quick_sort(lst))