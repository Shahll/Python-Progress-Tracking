""" 
1 2 3    1 4 7 
4 5 6 => 2 5 8 
7 8 9    3 6 9  
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated_martix = []

for col in range(len(matrix[0])-1, -1, -1):
    new_row = []
    for row in range(len(matrix[0])-1, -1, -1):
        new_row.append(matrix[row][col])
    rotated_martix.append(new_row)
    
for row in rotated_martix:
    print(row)