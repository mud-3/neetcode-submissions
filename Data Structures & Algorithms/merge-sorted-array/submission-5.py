class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        
        else:
            current1 = 0
            current2 = 0
            holder = 0

            while current1 < len(nums1) and current2 < len(nums2):
                if nums1[current1] < nums2[current2]:
                    current1 += 1
                    continue
                else:
                    holder = nums1[current1]
                    nums1[current1] = nums2[current2]
                    current1 += 1
                    current2 += 1

                    i = current1
                    while holder != 0:
                        temp = nums1[i]
                        nums1[i] = holder
                        holder = temp
                        i += 1
            
            if current2 < len(nums2):
                for i in range(m + current2, len(nums1)):
                    nums1[i] = nums2[current2]
                    current2 += 1