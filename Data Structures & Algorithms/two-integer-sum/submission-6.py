class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i in range(len(nums)):
            value = nums[i]
            if value in differences:
                return [differences[value], i]
            difference = target - value
            differences[difference] = i
            
