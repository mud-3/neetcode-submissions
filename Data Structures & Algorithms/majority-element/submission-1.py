class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        if threshold <= 1:
            return nums[0]

        hashmap = {}


        for num in nums:
            if num in hashmap:
                hashmap[num] += 1

                if hashmap[num] > threshold:
                    return num
            else:
                hashmap[num] = 1