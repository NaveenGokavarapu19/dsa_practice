nums = list(map(int,input().split())) 

#12 4 11 20 input 
# [4, 11, 12, 20] - output


n = len(nums)


for index in range(1,len(nums)):
    j = index
    while(j>=1):
        current_element = nums[j]
        previous_element = nums[j-1]
        if(current_element<previous_element):
            temp = current_element 
            nums[j] = previous_element
            nums[j-1] = temp
        j = j - 1 

print(nums)
            
        
    



        
        
        




