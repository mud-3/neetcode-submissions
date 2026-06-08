class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> copy;
        for (int num : nums) {
            if (num != val) {
                copy.push_back(num);
            }
        }
        nums = copy;

        return nums.size();
    }
};