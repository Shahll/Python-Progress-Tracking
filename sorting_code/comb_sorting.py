def comb_sort(array):
    gap = len(array)
    sorted = False
    while sorted == False:
        gap = int(gap // 1.3)
        if gap <= 0:
            sorted = True
            
        i = 0
        while i + gap != len(array) or i + gap < len(array):
            if array[i] > array[i + gap]:
                array[i + gap], array[i] = array[i] , array[i + gap]
            i += 1
    return array
# Driver       
lst = [8,4,1,56,3]
print(comb_sort(lst))
