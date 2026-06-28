class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left)// 2 #prevent overflow when l and r are large
            num = nums[mid]

            if num == target:
                return mid
            elif num > target:
                right = mid
            else:
                left = mid + 1
        
        return -1