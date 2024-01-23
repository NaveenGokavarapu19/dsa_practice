n = int(input())
nums = list(map(int,input().split())) 

for i in range(n):
    while nums[i] != i+1:
        temp = nums[i]
        nums[i] = nums[nums[i]-1]
        nums[temp-1] = temp

print(nums)