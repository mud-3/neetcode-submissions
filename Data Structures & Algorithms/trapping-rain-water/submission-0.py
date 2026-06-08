class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []

        max_height = 0
        for h in height:
            prefix.append(max_height)
            max_height = max(max_height, h)

        max_height = 0
        for h in reversed(height):
            suffix.append(max_height)
            max_height = max(max_height, h)
        
        suffix.reverse()
        
        total_water = 0

        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                total_water += water
        
        return total_water