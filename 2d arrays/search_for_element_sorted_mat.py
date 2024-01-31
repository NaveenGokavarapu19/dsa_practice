matrix = []
n = int(input())
target = int(input())

for i in range(n):
    to_add_matrix = list(map(int,input().split()))
    matrix.append(to_add_matrix)
    

flag = True
i = 0 
j = n-1 
while(((i<n) or (j>-1)) and flag):
    current_element = matrix[i][j]
    if(current_element>target):
        j = j - 1 
    if(current_element<target):
        i = i + 1 
    if(current_element == target):

        flag = False

if(flag):
    print("element not found")
else:
    print(f" Found at ({i},{j})")