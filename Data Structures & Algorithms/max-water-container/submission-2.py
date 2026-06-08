class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculateArea(left, right):
            return min(heights[left], heights[right]) * (right - left)

        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            water = calculateArea(left, right)
            maxWater = max(maxWater, water)

            if heights[left] < heights[right]: 
                left += 1
            else:
                right -= 1

        return maxWater