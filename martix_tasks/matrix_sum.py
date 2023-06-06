# Second option
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
new_matrix =[]
for row in range(len(matrix)):
    new_row = []
    for col in range(len(matrix[row])):
        new_row.append(matrix[col][row])
    new_matrix.append(new_row)
    
for row in new_matrix:
    print(row)
print()
# First option
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for row in range(len(matrix)):
    new_row = []
    for col in range(len(matrix[row])):
        new_row.append(matrix[row][col])
    print(new_row)