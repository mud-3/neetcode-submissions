class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {}

        for i in range(len(nums)):
            targets[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in targets and i != targets[nums[i]]:
                return [i, targets[nums[i]]]
