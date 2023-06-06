matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

temp = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] % 2 == 0:
            temp += matrix[row][col]
            
print(temp)