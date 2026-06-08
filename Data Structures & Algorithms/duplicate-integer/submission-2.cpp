class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> appeared;
        for (int num : nums) {
            if (appeared.find(num) != appeared.end()) {
                return true;
            } else {
                appeared.insert(num);
            }
        }
        return false;
    }
};