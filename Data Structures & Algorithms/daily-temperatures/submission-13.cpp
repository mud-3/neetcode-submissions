class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stack;
        vector<int> results(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); i++) {
            int current = temperatures[i];

            while (!stack.empty() && current > stack.top().second) {
                auto pair = stack.top();
                results[pair.first] = i - pair.first;
                stack.pop();
            }

            stack.push({i, current});
        }
        
        return results;
    }
};
