class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> results(temperatures.size(), 0);
        stack<pair<int, int>> storage;

        for (int i = 0; i < temperatures.size(); i++) {
            int current = temperatures[i];

            while (!storage.empty() && storage.top().second < current) {
                int index = storage.top().first;
                results[index] = i - index;
                storage.pop();
            }

            storage.push({i, current});
        }

        return results;
    }
};
