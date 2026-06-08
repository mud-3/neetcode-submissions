class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = 1

        for left in range(1, len(nums)):
            if (left == len(nums) - 1 or nums[left] != nums[left + 1]) and nums[left] != nums[right - 1]:
                nums[right] = nums[left]
                right += 1
                
        return right