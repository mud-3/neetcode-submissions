class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1, nums[0]]
        suffixes = [1, nums[-1]]
        
        for i in range(1, len(nums) - 1):
            prefixes.append(prefixes[i] * nums[i])
            suffixes.append(suffixes[i] * nums[-i - 1])
        answer = []

        for i in range(len(nums)):
            answer.append(prefixes[i] * suffixes[-i - 1])

        return answer