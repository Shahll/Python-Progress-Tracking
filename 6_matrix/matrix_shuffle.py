import random

matrix = [[3, 1, 5],
          [2, 3, 0],
          [4, 1, 2]]
array = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        array.append(matrix[row][col])

random.shuffle(array)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix[row][col] = array[row * len(matrix[row]) + col]
        
for row in matrix:
    print(row)
