matrix = [[6, 29, 91, 9, 10],
          [11, 12, 53, 14, 15],
          [16, 70, 18, 39, 20],
          [21, 22, 23, 24, 25]]

highest = 0
row_index = 0
col_index = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if highest < (matrix[row][col]):
            highest = matrix[row][col]
            row_index = row
            col_index = col
print(highest, row_index, col_index)