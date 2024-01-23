class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 1
        max_count = 0
        if(n==1):
            return 1
        for index in range(n-1):
            current_element = nums[index]
            next_element = nums[index+1]
            if(current_element +1 == next_element):
                count = count + 1 
            else:
                max_count = max(count,max_count)
                count = 1

            if(max_count == 1 and index == n-2):
                max_count = max(max_count,count)

        return max_count