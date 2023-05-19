def merge(left,right):
    merge = []
    while left != [] and right != []:
        if left[0] > right[0]:
            merge.append(right.pop(0))
        else:
            merge.append(left.pop(0))
            
    merge += left
    merge += right
    return merge

def merge_sort(array):
    if len(array) // 2 <=1:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[mid:])
    right = merge_sort(array[:mid])
    
    return merge(left,right)

# Driver
lst = [8,5,2,6,0,1,3,14,7]
print(merge_sort(lst))
