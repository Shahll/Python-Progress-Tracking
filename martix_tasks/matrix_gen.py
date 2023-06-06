matrix = []
rows = 4
cols = 5
i = 5
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        i += 1
        if row == rows -1 and col == cols - 1:
            break
        else:
            matrix[row].append(i)
            
print(matrix)