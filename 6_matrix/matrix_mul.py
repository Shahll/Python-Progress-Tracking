def mul_matrix(a, b):
    result_matrix = []
    
    if len(a[0]) != len(b):
        return None    

    for row_a in range(len(a)): # 0 1     1 2
        new_row = []
        for col_b in range(len(b[0])): # 0 1 2 3     1 2 3 4
            element = 0
            for col_a in range(len(b)): # 0 1 2     1 2 3
                element += a[row_a][col_a] * b[col_a][col_b]
            new_row.append(element)
        result_matrix.append(new_row)
    
    return result_matrix

matrix_a = [[0, 1, 2],
            [1, 2, 2]]

matrix_b = [[0, 1, 2, 3],
            [1, 1, 3, 3],
            [2, 2, 3, 5]]

print(mul_matrix(matrix_a, matrix_b))