class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        number_set = set(nums)
        if(n == 0):
            return 0

        max_len = 1
        for index in range(n):
            current_element = nums[index]
            before_element = current_element - 1 
            if(before_element not in number_set):
                length = 0
                num = current_element
                while num in number_set:
                    length = length + 1
                    num = num + 1
                max_len = max(length,max_len)
        return max_len