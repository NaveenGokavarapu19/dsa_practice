

# this question is for N/2 majority

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element = nums[0]
        max_count=0
        count = 0
        for element in nums:
            if(element == majority_element):
                count  = count + 1 
                max_count = max(count,max_count)
            elif (element != majority_element):
                count = count -1 
            if(count<0):
                count = 0 
                majority_element = element 

        return majority_element