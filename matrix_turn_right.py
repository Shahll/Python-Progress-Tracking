""" 
1 2 3    7 4 1
4 5 6 => 8 5 2 
7 8 9    9 6 3 
"""
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated_martix = []

for col in range(len(matrix[0])):
    new_row = []
    for row in range(len(matrix[0]) -1, -1, -1):
        new_row.append(matrix[row][col])
    rotated_martix.append(new_row)
    
for row in rotated_martix:
    print(row)
