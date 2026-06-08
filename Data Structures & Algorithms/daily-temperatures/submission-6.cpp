class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int last = temperatures[0];
        vector<int> key_storage = {0};
        vector<int> results = {0};
        for (int i = 1; i < temperatures.size(); i++) {
            int current = temperatures[i];
            results.push_back(0);
            if (current > last) {
                for (int j = key_storage.size() - 1; j >= 0; j--) {
                    int key = key_storage[j];
                    int value = temperatures[key];
                    if (value < current) {
                        results[key] = i - key;
                        key_storage.pop_back();
                    }
                }
            }
            key_storage.push_back(i);
            last = current;
        }
        return results;
    }
};
