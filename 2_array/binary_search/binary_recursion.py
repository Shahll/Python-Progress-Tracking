def findMe(array, target, start, end):
    if start > end:
        return "Not Found"

    middle = (start + end) // 2

    if array[middle] == target:
        return f"Found it at index {middle}"

    if array[middle] > target:
        return findMe(array, target, start, middle - 1)

    if array[middle] < target:
        return findMe(array, target, middle + 1, end)
# Driver
array = ['a', 'b', 'c', 'x', 'y', 'z']
print(findMe(array, "y", 0, len(array) - 1))
