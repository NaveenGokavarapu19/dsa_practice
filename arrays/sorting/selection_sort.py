from sys import maxsize
nums = list(map(int,input().split())) 

n = len(nums)
# 11 25 12 22 64


for i in range(n):
    j = i 
    mini = maxsize
    smallest_index = 0
    while(j<n):
        current_element = nums[j]
        if(current_element<mini):
            mini = current_element
            smallest_index = j
        j = j + 1 
    temp = nums[i]
    nums[i] = nums[smallest_index]
    nums[smallest_index] = temp 
    
print(nums)