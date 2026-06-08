class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left <= right:
            rate = (left + right) // 2
            time = 0

            for pile in piles:
                time += (pile + rate - 1) // rate
                if time > h:
                    break
            
            if time > h:
                left = rate + 1
            else:
                right = rate - 1
        
        return left
