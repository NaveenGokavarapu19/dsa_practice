n = int(input())
matrix = []

for _ in range(n):
    rows = list(map(int,input().split()))
    matrix.append(rows)
    
# tranpose first 

for row in range(n):
    for col in range(n):
        if(row>col):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

# rotate the matrix by 90 clockwise

print(matrix)


# for 180 degrees rotation rotate the matrix 2 times 
# use the below code for clockwise 
for k in range(n):
    i = 0
    j = n-1
    while (i<j):
        temp = matrix[k][i] 
        matrix[k][i] = matrix[k][j]
        matrix[k][j] = temp 
        i = i + 1 
        j = j -1


#  uncomment the below code for anticlockwise
        
# for k in range(n):
#     i = 0
#     j = n-1
#     while (i<j):
#         temp = matrix[i][k] 
#         matrix[i][k] = matrix[j][k]
#         matrix[j][k] = temp 
#         i = i + 1 
#         j = j -1
        
print(matrix)
     
 
