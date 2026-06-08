class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, target in enumerate(nums):
            if target > 0:
                break #all positive, impossible to add up to zero

            if i > 0 and target == nums[i - 1]:
                continue #same number, keep going
            #2 sum algorithm
            start, end = i + 1, len(nums) - 1
            while start < end:
                threeSum = target + nums[start] + nums[end]
                if threeSum > 0:
                    end -= 1 #too big, so decrease end
                elif threeSum < 0:
                    start += 1 #too small, so increase start
                else:
                    res.append([target, nums[start], nums[end]]) #add into solution
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1 #search for next distinct number
                        
        return res