class Solution:
    #optimal solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        preproducts = postproducts = 1

        for i in range(len(nums)):
            answer[i] = preproducts
            preproducts *= nums[i]
        
        for i in range(1, len(nums) + 1):
            answer[-i] *= postproducts
            postproducts *= nums[-i]

        return answer