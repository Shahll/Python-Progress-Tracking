""" 
Відсортувати матрицю
3 1 5    0 1 1 
2 3 0 => 2 2 3 
4 1 2    3 4 5
"""
matrix = [[3, 1, 5],
          [2, 3, 0],
          [4, 1, 2]]
array = []

for row in range(len(matrix[0])):
    for col in range(len(matrix[0])):
        array.append(matrix[row][col])

array = sorted(array)

for row in range(len(matrix[0])):
    for col in range(len(matrix[0])):
        matrix[row][col] = array[row * len(matrix[row]) + col]
        
for row in matrix:
    print(row)
        