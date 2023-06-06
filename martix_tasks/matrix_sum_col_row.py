matrix = [[6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24]]



for col in range(len(matrix[0])):
    sum_col = 0
    for row in range(len(matrix)):
        if col < len(matrix[row]):
            sum_col += matrix[row][col]
    print(f"{col} col sum: {sum_col}")
    
print()

for row in range(len(matrix)):
    sum_row = 0
    for col in range(len(matrix[row])):
        sum_row += matrix[row][col]
    print(f"{row} row sum: {sum_row}")
