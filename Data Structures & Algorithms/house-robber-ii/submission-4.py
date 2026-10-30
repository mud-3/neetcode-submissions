class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        rob1, rob2 = 0, 0
        rob3, rob4 = 0, 0

        for num in nums[:-1]:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        for num in nums[1:]:
            temp = max(num + rob3, rob4)
            rob3 = rob4
            rob4 = temp
        
        return max(rob2, rob4)