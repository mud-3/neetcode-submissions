class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_rate = 0
        
        while left <= right:
            time = h
            rate = (left + right) // 2

            for pile in piles:
                time -= math.ceil(pile / rate)

                if time < 0:
                    left = rate + 1
                    break
            
            if time >= 0:
                right = rate - 1
                if min_rate == 0 or rate < min_rate:
                    min_rate = rate

        return min_rate

