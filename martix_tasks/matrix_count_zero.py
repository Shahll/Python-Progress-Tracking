matrix = [[0, 29, 91, 9, 10],
          [11, 12, 53, 14, 15],
          [16, 70, 18, 0, 0],
          [0, 22, 23, 24, 25]]

counter = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 0:
            counter += 1
            
print(counter)