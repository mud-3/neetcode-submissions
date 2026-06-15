class Solution:
    #my original solution, bad news: wasted too much space/memory
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        suffixes = [1]
        
        for i in range(len(nums)):
            prefixes.append(prefixes[i] * nums[i])
            suffixes.append(suffixes[i] * nums[-i - 1])

        answer = []

        for i in range(len(nums)):
            answer.append(prefixes[i] * suffixes[-i - 2])

        return answer