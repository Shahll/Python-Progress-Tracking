cols = 2 
rows = 3 
m = [[0, 0, 0], [0, 0, 0]]   

for i in range(cols): 

    for j in range(rows):
        user = int(input(f"Enter a number for {i}{j} "))
        m[i][j] = user
    
    
print(m)