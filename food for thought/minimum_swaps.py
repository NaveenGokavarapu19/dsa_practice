# for array starting from 0
# food for thought
 

nums = list(map(int,input().split())) 
n = len(nums)

for index,element in enumerate(nums):
    current_element = nums[index]
    destination_element = nums[nums[index]-1]
    
    while nums[index] != index+1:
        temp = current_element
        nums[index] = destination_element
        nums[temp-1] = current_element

print(nums)