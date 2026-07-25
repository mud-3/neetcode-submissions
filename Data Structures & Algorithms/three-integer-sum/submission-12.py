class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()

        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            target = - nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                twoSum = nums[left] + nums[right]
                if twoSum == target:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left] and nums[right + 1] == nums[right]:
                        left += 1
                        right -= 1
                elif twoSum > target:
                    right -= 1
                else:
                    left += 1
                    
        return solution