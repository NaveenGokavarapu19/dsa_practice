class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_array = [0]*n
        count = 0
        for index,element in enumerate(nums):
            if(element!=0):
                new_array[count] = element 
                count = count + 1

        for index,element in enumerate(new_array):
            nums[index] = element
        