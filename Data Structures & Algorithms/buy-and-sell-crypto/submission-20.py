class Solution:
    #my first solution
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]

        for sell in prices:
            if sell > buy:
                max_profit = max(max_profit, sell - buy)
            else:
                buy = sell
        
        return max_profit
