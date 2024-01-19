class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for index in range(1,n):
            current_element =  nums[index]
            previous_element = nums[index-1]
            if(current_element == previous_element):
                return current_element