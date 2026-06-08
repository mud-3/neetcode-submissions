class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in results:
                return [results[diff], i]
            results[num] = i