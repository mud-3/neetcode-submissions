class Solution:
    #hashset
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = list(set(nums))
        count = longest = 1

        for num in nums:
            while num + 1 in nums:
                num += 1
                count += 1
            longest = max(longest, count)
            count = 1
        
        return longest
        