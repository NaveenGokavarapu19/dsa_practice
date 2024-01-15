n = int(input())
nums = list(map(int,input().split())) 
k = int(input())
count = 0
target_list = [0]*n

for index in range(n):
    dest_index = index - k 
    if(dest_index<0):
        dest_index = dest_index + n
    target_list[dest_index] = nums[index]
    
print(target_list)