class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for index,element in enumerate(nums):
            difference = target - element
            if difference in sum_map:
                list1 = []
                list1.append(sum_map[difference])
                list1.append(index)
                return list1
            else:
                sum_map[element]=sum_map.get(element,index)

            
        