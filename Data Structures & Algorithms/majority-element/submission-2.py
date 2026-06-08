class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        if threshold <= 1:
            return nums[0]

        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

            if hashmap[num] > threshold:
                return num