array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix = []

for i in range(3):
    matrix.append([])
    for j in range(3):
        matrix[i].append(array[j + i * 3])

        
print(matrix)