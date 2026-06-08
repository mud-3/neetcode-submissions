class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] < nums[r]:
                r = m
            
            else:
               l = m + 1

        def binary_search(section, target, starting):
            l = 0
            r = len(section) - 1

            while l <= r:
                m = l + (r - l) // 2

                if section[m] > target:
                    r = m - 1
                elif section[m] < target:
                    l = m + 1
                else:
                    return m + starting
            
            return -1

        return max(binary_search(nums[l:], target, l), binary_search(nums[:l], target, 0))