class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0;
        int sell = 1;
        int max_profit = 0;
        while (buy < prices.size() - 1) {
            int profit = prices[sell] - prices[buy];
            if (profit > max_profit) {
                max_profit = profit;
            }
            sell++;
            if (sell == prices.size()) {
                buy++;
                sell = buy + 1;
            }
        }
        return max_profit;
    }
};
