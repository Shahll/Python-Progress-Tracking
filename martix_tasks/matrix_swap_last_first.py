""" 
Замінити місцями перший і останній стовпчик матриці 
 1  2  3  4  5     5  2  3  4  1 
 6  7  8  9 10    10  7  8  9  6 
11 12 13 14 15 => 15 12 13 14 11 
16 17 18 19 20    20 17 18 19 16 
21 22 23 24 25    25 22 23 24 21 
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
temp = None
for row in range(len(matrix[0])):
    sub_row = []
    for col in range(len(matrix[0])):
        sub_row.append(matrix[row][col])
    if row == 0:
        temp = sub_row
matrix[0] = sub_row
matrix[len(matrix) -1] = temp
print(matrix)