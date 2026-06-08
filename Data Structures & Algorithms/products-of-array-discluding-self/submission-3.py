class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_0 = 1
        non0_count = 0
        for num in nums:
            product *= num
            if num != 0:
                product_0 *= num
                non0_count += 1
        
        if non0_count <= len(nums) - 2:
            product = product_0 = 0

        output = []
        for num in nums:
            if num != 0:
                output.append(int(product / num))
            else:
                output.append(product_0)
        
        return output

