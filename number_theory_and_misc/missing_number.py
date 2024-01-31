class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing_element = n
        for i in range(len(nums)):
            while nums[i] != -1 and nums[i] < n and nums[i] != i:
                if nums[i] != nums[nums[i]]:
                    x = nums[i]
                    nums[i] = nums[nums[i]]
                    nums[x] = x

        for index, element in enumerate(nums):
            if index != element:
                missing_element = index
        return missing_element