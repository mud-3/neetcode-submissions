class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0;
        int sell = 1;
        int max_profit = 0;
        while (sell < prices.size()) {
            int profit = prices[sell] - prices[buy];
            if (profit > 0) {
                if (profit > max_profit) {
                    max_profit = profit;
                }
            } else {
                buy = sell;
            }
            sell++;
        }
        return max_profit;
    }
};
