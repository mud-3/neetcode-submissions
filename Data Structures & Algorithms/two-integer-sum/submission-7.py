class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, n in enumerate(nums):
            if n in differences:
                return [differences[n], i]
            difference = target - n
            differences[difference] = i