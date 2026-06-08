class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy = []
        for num in nums:
            if num != val:
                copy.append(num)
        nums[:] = copy
        return len(copy)