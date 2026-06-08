class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = 0

        for i in range(len(nums)):
            num = nums[abs(nums[i]) - 1]
            print(nums)
            if num < 0:
                return abs(nums[i])

            nums[abs(nums[i]) - 1] *= -1

        return abs(nums[i])