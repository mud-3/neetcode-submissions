class Solution:
    #solution with better
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            current_price = prices[i]
            min_price = min(min_price, current_price)
            max_profit = max(max_profit, current_price - min_price)
        
        return max_profit